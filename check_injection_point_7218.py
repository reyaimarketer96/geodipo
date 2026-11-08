import json

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\157\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')
idx = content.find('Kredensial Otoritas')
if idx != -1:
    print("Found 'Kredensial Otoritas' at:", idx)
    print("Preceding 300 chars:")
    print(content[idx-300:idx])
