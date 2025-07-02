import pandas as pd

FILE_PATH = '../data/2024_fb_posts_president_scored_anon.csv'

def main():
    df = pd.read_csv(FILE_PATH)
    print(f"Loaded {len(df)} rows\n")

    # Basic stats
    print("Overall describe():\n")
    print(df.describe(include='all'))

    # Non-numeric columns: value counts
    print("\nTop value counts for non-numeric columns:")
    non_numeric_cols = df.select_dtypes(include='object').columns

    for col in non_numeric_cols:
        print(f"\n{col}:")
        print(df[col].value_counts().head(3))
        print(f"Unique count: {df[col].nunique()}")

    # Group by Facebook_Id
    print("\nGrouped by Facebook_Id (showing stats for first 3 groups):")
    grouped = df.groupby('Facebook_Id')
    for group, sub_df in list(grouped)[0:3]:
        print(f"\nGroup: {group}")
        print(sub_df.describe(include='all'))

if __name__ == '__main__':
    main()