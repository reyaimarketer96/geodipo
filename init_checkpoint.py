import json

initial_checkpoint = {
    "completed_ids": [3073, 7218, 111, 4288],
    "already_enriched_ids": [3073, 7218, 111, 4288],
    "failed_ids": []
}

with open("checkpoint.json", "w", encoding="utf-8") as f:
    json.dump(initial_checkpoint, f, indent=2, ensure_ascii=False)

print("Initialized checkpoint.json with 4 pilot IDs.")
