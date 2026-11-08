import json
import os
import re

with open("audit/raw_all_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

with open("audit/raw_all_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

print(f"Total posts: {len(posts)}")
print(f"Total pages: {len(pages)}")

# Load RAG canonical regions
rag_db_path = "rag_knowledge_base/database"
regions = os.listdir(rag_db_path)
print(f"Total RAG regions available: {len(regions)}")

# Inspect category distribution in posts
cat_counts = {}
for p in posts:
    cats = tuple(p.get("categories", []))
    cat_counts[cats] = cat_counts.get(cats, 0) + 1

print("\nPost categories distribution:")
for k, v in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  Category {k}: {v} posts")

# Sample some slugs
print("\nSample post slugs:")
for p in posts[:10]:
    print(f"  ID {p['id']}: {p['slug']} ({p['title']['rendered']})")

print("\nSample page slugs:")
for p in pages[:10]:
    print(f"  ID {p['id']}: {p['slug']} ({p['title']['rendered']})")
