import pandas as pd

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()
    # Fill missing values
    df = df.fillna(df.mean(numeric_only=True))
    return df

def generate_summary(df):
    return df.describe()
