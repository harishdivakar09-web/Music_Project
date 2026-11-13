import pandas as pd

df = pd.read_csv("query.csv")

df = df.drop('musician', axis=1)
df['birthDate'] = df['birthDate'].str.split("T").str[0].str.strip().to_datetime()
df['deathDate'] = df['deathDate'].str.split("T").str[0].str.strip().to_datetime()

df
print(df.head())
print(df.isna().sum())