import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\362\output.txt', 'r', encoding='utf-8') as f:
    post = json.load(f)

print('Title:', post.get('title'))
print('Slug:', post.get('slug'))
content = post.get('content', '')
print('Content length:', len(content))
clean_text = re.sub(r'<[^>]+>', ' ', content)
clean_text = ' '.join(clean_text.split())
print('Content snippet:', clean_text[:400])
