import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')

# Extract section with id 'geologi-kudus' or 'data-lokal-kudus'
pattern = r'<section[^>]*id=["\'](geologi-kudus|akuifer-kudus|data-lokal-kudus)["\'][^>]*>(.*?)</section>'
matches = re.findall(pattern, content, re.DOTALL)
for sec_id, sec_content in matches:
    print(f'=== SECTION ID: {sec_id} ===')
    print(f'Length: {len(sec_content)}')
    # clean tags for preview
    clean_text = re.sub(r'<[^>]+>', ' ', sec_content)
    clean_text = ' '.join(clean_text.split())
    print(f'Text snippet: {clean_text[:400]}...\n')
