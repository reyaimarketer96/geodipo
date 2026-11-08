import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', content)
print('Sections found:', sections)

headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
print(f'Total headings: {len(headings)}')
for h in headings[:15]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    print(' -', clean)
