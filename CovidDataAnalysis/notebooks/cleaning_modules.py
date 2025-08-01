import numpy as np
import pandas as pd


def set_dtypes(df, columns):
    for col in columns:

        if not np.issubdtype(df[col].dtype, np.number):
            continue

        if df[col].dropna().empty:
            continue


        if df[col].dropna().apply(lambda x: isinstance(x, (int, float)) and x == int(x)).all():
            max_val = df[col].max()
            min_val = df[col].min()

            if min_val >= 0:
                # عدد صحیح بدون علامت
                if max_val < 2 ** 8:
                    target_dtype = 'UInt8'
                elif max_val < 2 ** 16:
                    target_dtype = 'UInt16'
                elif max_val < 2 ** 32:
                    target_dtype = 'UInt32'
                else:
                    target_dtype = 'UInt64'
            else:
                # عدد صحیح با علامت
                if -128 <= min_val <= 127 and max_val <= 127:
                    target_dtype = 'Int8'
                elif -32768 <= min_val <= 32767:
                    target_dtype = 'Int16'
                elif -2 ** 31 <= min_val <= 2 ** 31 - 1:
                    target_dtype = 'Int32'
                else:
                    target_dtype = 'Int64'
        else:
            target_dtype = 'float32'

        try:
            df[col] = df[col].astype(target_dtype)
            print(f"{col} → {target_dtype}")
        except Exception as e:
            print(f"{col} could not be converted to {target_dtype}: {e}")

        return df


def to_numeric_func(df,columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')


def country_nan_percentage(df, group_col, target_col='deaths'):
    result = (df.groupby(group_col)[target_col].apply(lambda x: x.isna().mean() * 100).sort_values(ascending=False))
    for country, percent in result.items():
        print(f"{country} : {percent:.2f}%")



def columns_nan_percentage(df):
    nan_percent = df.isna().mean() * 100
    return nan_percent[nan_percent >= 0].sort_values(ascending=False)



