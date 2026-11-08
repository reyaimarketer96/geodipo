import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\157\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

print('Title:', page.get('title'))
print('Status:', page.get('status'))
content = page.get('content', '')
print('Content length:', len(content))
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', content)
print('Sections found in 7218:', sections)
headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
print(f'Total headings: {len(headings)}')
for h in headings[:10]:
    print(' -', re.sub(r'<[^>]+>', '', h).strip())
