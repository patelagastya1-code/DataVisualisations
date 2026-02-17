"""
Build a single HTML file with embedded data for offline use.
Run: python build_html.py
"""
import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('index_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject data - replace the placeholder
html = html.replace('__DATA_PLACEHOLDER__', json.dumps(data))
print("Built index.html with embedded data")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
