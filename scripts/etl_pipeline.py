"""
ETL pipeline for Capstone 2 - Online Retail Analytics
Loads raw excel, cleans it, adds new columns, saves to processed/
"""

from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import numpy as np


def load_raw(path: Path) -> pd.DataFrame:
    if str(path).endswith('.xlsx'):
        return pd.read_excel(path)
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # duplicates
    df = df.drop_duplicates()

    # missing customer IDs - keep as Guest instead of dropping
    df['CustomerID'] = df['CustomerID'].fillna(0).astype(int).astype(str)
    df['CustomerID'] = df['CustomerID'].replace('0', 'Guest')

    # missing descriptions
    df['Description'] = df['Description'].fillna('Unknown').astype(str).str.strip().str.upper()

    # remove system entries
    junk = ['POSTAGE', 'DOTCOM POSTAGE', 'CRUK COMMISSION', 'MANUAL', 'BANK CHARGES', 'AMAZON FEE']
    df = df[~df['Description'].isin(junk)]

    # bad quantity/price rows
    is_cancel = df['InvoiceNo'].astype(str).str.startswith('C')
    df = df[~((df['Quantity'] < 0) & (~is_cancel))]
    df = df[df['UnitPrice'] > 0]

    # flag cancellations
    df['IsCancelled'] = df['InvoiceNo'].astype(str).str.startswith('C')

    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceYearMonth'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    df['MonthName'] = df['InvoiceDate'].dt.strftime('%B')
    df['MonthNumber'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    df['Quarter'] = 'Q' + df['InvoiceDate'].dt.quarter.astype(str)
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['IsUK'] = df['Country'].apply(lambda x: 'UK' if x == 'United Kingdom' else 'International')

    def tod(h):
        if 5 <= h < 12: return 'Morning'
        elif 12 <= h < 17: return 'Afternoon'
        elif 17 <= h < 21: return 'Evening'
        else: return 'Night'
    df['TimeOfDay'] = df['Hour'].apply(tod)

    basket = df.groupby('InvoiceNo').agg(
        BasketTotal=('TotalRevenue', 'sum'),
        ItemsPerOrder=('Quantity', 'sum')
    ).reset_index()

    def bsize(v):
        if v < 50: return 'Small'
        elif v <= 200: return 'Medium'
        else: return 'Large'
    basket['BasketSize'] = basket['BasketTotal'].apply(bsize)
    df = df.merge(basket[['InvoiceNo', 'BasketSize', 'ItemsPerOrder']], on='InvoiceNo', how='left')

    cust = df[df['CustomerID'] != 'Guest'].groupby('CustomerID').agg(
        OrderCount=('InvoiceNo', 'nunique'),
        TotalSpend=('TotalRevenue', 'sum')
    ).reset_index()
    cust['AvgOrderValue'] = (cust['TotalSpend'] / cust['OrderCount']).round(2)
    cust['IsRepeatCustomer'] = cust['OrderCount'].apply(lambda x: 'Repeat' if x > 1 else 'One-Time')
    df = df.merge(cust[['CustomerID', 'AvgOrderValue', 'IsRepeatCustomer']], on='CustomerID', how='left')
    df['IsRepeatCustomer'] = df['IsRepeatCustomer'].fillna('Guest')
    df['AvgOrderValue'] = df['AvgOrderValue'].fillna(0)

    return df


def save(df: pd.DataFrame, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    return p.parse_args()


def main():
    args = parse_args()
    df = load_raw(args.input)
    print(f'Loaded: {df.shape}')
    df = clean(df)
    df = add_features(df)
    save(df, args.output)
    print(f'Saved to {args.output} | shape: {df.shape}')


if __name__ == '__main__':
    main()
