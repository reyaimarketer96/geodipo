import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\157\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')
keywords = ['jurnal', 'skripsi', 'tesis', 'peneliti', 'sudaryanto', 'hidayat', 'undip', 'itb', 'ugm', 'sitasi', 'pustaka']
for kw in keywords:
    count = content.lower().count(kw)
    print(f"Keyword '{kw}': {count} occurrences")
