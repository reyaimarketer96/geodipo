import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')
links = re.findall(r'href=["\']([^"\']+)["\']', content)
internal = [l for l in links if 'geodipo.com' in l or (l.startswith('/') and not l.startswith('//'))]
print(f"Total internal links in Page 111 (jasa-sumur-bor-kudus): {len(internal)}")
unique_internal = sorted(list(set(internal)))
print(f"Unique internal links: {len(unique_internal)}")
for l in unique_internal[:15]:
    print(" -", l)
