#!/bin/bash
python3 -c "
import json
with open('checkpoint.json', encoding='utf-8') as f:
    cp = json.load(f)
with open('rag_knowledge_base/mappings/unified_queue.json', encoding='utf-8') as f:
    q = json.load(f)
completed = len(set(cp.get('completed_ids', []) + cp.get('already_enriched_ids', [])))
total = len(q)
pct = (completed / total) * 100
failed = len(cp.get('failed_ids', []))
print('==================================================')
print(f' GEODIPO RAG INJECTION PROGRESS: {completed}/{total} ({pct:.1f}%)')
print(f' Completed: {len(cp.get(\"completed_ids\", []))}')
print(f' Pre-existing / Skipped: {len(cp.get(\"already_enriched_ids\", []))}')
print(f' Failed / Retry Needed: {failed}')
print('==================================================')
"
