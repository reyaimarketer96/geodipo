"""
Direct REST Deployment Test for Page 3073 (KITB Batang)
"""

import os
import json
import requests

token = os.environ.get("GEODIPO_TOKEN")
if not token:
    raise ValueError("GEODIPO_TOKEN not found in environment.")

url = "https://geodipo.com/wp-json/wp/v2/pages/3073"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

with open("deployment/backups/rag_injection/prepared_page_3073.txt", "r", encoding="utf-8") as f:
    new_content = f.read()

payload = {
    "content": new_content
}

print(f"Sending POST to {url} (Content length: {len(new_content)})...")
resp = requests.post(url, headers=headers, json=payload, timeout=30)
print(f"Response status: {resp.status_code}")

if resp.status_code == 200:
    res_data = resp.json()
    print("Deployment successful!")
    print(f"Page ID: {res_data.get('id')}")
    print(f"Modified: {res_data.get('modified')}")
    print(f"Link: {res_data.get('link')}")
else:
    print(f"Error {resp.status_code}: {resp.text[:500]}")
