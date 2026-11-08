import json
import re

with open(r'C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt', 'r', encoding='utf-8') as f:
    page = json.load(f)

content = page.get('content', '')

# Find where data-lokal-kudus ends
idx = content.find('id="data-lokal-kudus"')
if idx != -1:
    end_sec = content.find('</section>', idx)
    print("Context around end of data-lokal-kudus:")
    print(content[end_sec-200:end_sec+300])
