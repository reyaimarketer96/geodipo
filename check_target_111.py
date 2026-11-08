import json

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')
target = 'id="proses-pemesanan-sumur-bor-kudus"'
idx = content.find(target)
sec_start = content.rfind('<section', 0, idx)
sec_end = content.find('>', idx) + 1
full_tag = content[sec_start:sec_end]
print('Full tag:', repr(full_tag))
