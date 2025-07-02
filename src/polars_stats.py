import polars as pl

FILE_PATH = '../data/2024_fb_posts_president_scored_anon.csv'

def main():
    df = pl.read_csv(FILE_PATH)

    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns\n")

    # Overall numeric stats
    print("=== Overall Descriptive Statistics ===")
    print(df.describe())

    # Top value counts for non-numeric fields
    print("\n=== Top Value Counts (non-numeric fields) ===")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            vc = df[col].value_counts().sort('count', descending=True).limit(3)
            print(f"\n{col}:")
            print(vc)

    # Grouped stats
    print("\n=== Grouped by Facebook_Id (first 3 groups) ===")
    groups = df.group_by("Facebook_Id")

    for group_key, group_df in list(groups)[:3]:
        print(f"\nGroup: Facebook_Id={group_key[0]}")
        print(group_df.describe())

if __name__ == "__main__":
    main()