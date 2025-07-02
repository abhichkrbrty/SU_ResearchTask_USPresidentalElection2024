import csv
from collections import defaultdict, Counter
from statistics import mean

# === CONFIG ===
FILE_PATH = '../data/2024_fb_posts_president_scored_anon.csv'
PRIMARY_GROUP_COL = 'Facebook_Id'
SECONDARY_GROUP_COL = 'post_id'  # Change to 'ad_id' if you work with ad data

# === HELPERS ===

def is_float(value):
    try:
        float(value.replace(",", ""))  # Handle commas like "50,629"
        return True
    except:
        return False

def to_float(value):
    return float(value.replace(",", "")) if is_float(value) else None

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_column_stats(rows):
    stats = {}
    colnames = rows[0].keys()

    for col in colnames:
        values = [row[col] for row in rows if row[col] not in ('', None)]
        if not values:
            continue

        if all(is_float(v) for v in values):
            nums = list(map(to_float, values))
            stats[col] = {
                'count': len(nums),
                'mean': round(mean(nums), 2),
                'min': min(nums),
                'max': max(nums),
            }
        else:
            freq = Counter(values)
            stats[col] = {
                'count': len(values),
                'unique': len(freq),
                'most_common': freq.most_common(1)[0]
            }

    return stats

def group_by(rows, key):
    grouped = defaultdict(list)
    for row in rows:
        if key in row:
            grouped[row[key]].append(row)
    return grouped

def group_by_two_keys(rows, key1, key2):
    grouped = defaultdict(list)
    for row in rows:
        if key1 in row and key2 in row:
            grouped[(row[key1], row[key2])].append(row)
    return grouped

# === MAIN ===

def main():
    rows = load_data(FILE_PATH)
    print(f"Loaded {len(rows)} rows\n")

    # Overall stats
    print("Overall Dataset Stats:\n")
    overall_stats = get_column_stats(rows)
    for col, stat in overall_stats.items():
        print(f"{col}: {stat}")

    # Group by primary key
    print(f"\nGrouped by {PRIMARY_GROUP_COL} (showing top 3 groups):")
    grouped = group_by(rows, PRIMARY_GROUP_COL)
    for group_id, group_rows in list(grouped.items())[:3]:
        print(f"\nStats for {PRIMARY_GROUP_COL}={group_id}:")
        stats = get_column_stats(group_rows)
        for k, v in stats.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()