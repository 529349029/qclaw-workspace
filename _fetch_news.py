import urllib.request, xml.etree.ElementTree as ET, sys, json

def fetch_rss(url, label):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            xml_data = r.read()
        root = ET.fromstring(xml_data)
        items = []
        for item in root.findall('.//item'):
            title = (item.findtext('title') or '').strip()
            desc = (item.findtext('description') or '').strip()
            pub = (item.findtext('pubDate') or '').strip()
            if title:
                items.append({'title': title, 'desc': desc, 'pub': pub})
        return label, items
    except Exception as e:
        return label, [str(e)]

# Fetch from multiple sources
sources = [
    ("https://feeds.bbci.co.uk/news/world/rss.xml", "BBC 世界"),
    ("https://feeds.bbci.co.uk/news/business/rss.xml", "BBC 商业"),
    ("https://feeds.bbci.co.uk/news/technology/rss.xml", "BBC 科技"),
    ("https://feeds.bbci.co.uk/news/uk/rss.xml", "BBC 英国"),
]

all_results = {}
for url, label in sources:
    label, items = fetch_rss(url, label)
    all_results[label] = items
    print(f"Fetched {len(items)} items from {label}")

with open(r"C:\Users\Administrator\.qclaw\workspace\_news_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print("Done. Saved to _news_raw.json")
