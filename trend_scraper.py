import requests
import json
import pandas as pd
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

session = requests.Session()
session.headers.update(HEADERS)

# -------------------------
# Step 1 — Get cookies
# -------------------------
session.get("https://trends.google.com")

# -------------------------
# Config
# -------------------------
KEYWORDS = [
    "ai tools",
    "online course",
    "electric scooter",
    "protein powder",
    "freelance"
]

TIMEFRAME = "today 12-m"
GEO = ""

# -------------------------
# Step 2 — Get widget tokens
# -------------------------
def get_widgets(keyword):
    url = "https://trends.google.com/trends/api/explore"

    params = {
        "hl": "en-US",
        "tz": "360",
        "req": json.dumps({
            "comparisonItem": [{
                "keyword": keyword,
                "geo": GEO,
                "time": TIMEFRAME
            }],
            "category": 0,
            "property": ""
        })
    }

    r = session.get(url, params=params)
    text = r.text[5:]   # remove )]}',
    data = json.loads(text)

    for w in data["widgets"]:
        if w["id"] == "TIMESERIES":
            return w

    raise Exception("Timeseries widget not found")

# -------------------------
# Step 3 — Pull interest data
# -------------------------
def get_trend_data(widget):
    url = "https://trends.google.com/trends/api/widgetdata/multiline"

    payload = {
        "req": json.dumps(widget["request"]),
        "token": widget["token"],
        "tz": "360"
    }

    r = session.get(url, params=payload)
    print(r)
    text = r.text[5:]   # remove )]}',
    return json.loads(text)

# -------------------------
# Step 4 — Collect all keywords
# -------------------------
all_series = {}

for kw in KEYWORDS:
    print("Fetching:", kw)

    widget = get_widgets(kw)
    data = get_trend_data(widget)

    timeline = data["default"]["timelineData"]

    series = {}
    for point in timeline:
        date = point["formattedTime"]
        value = point["value"][0]
        series[date] = value

    all_series[kw] = series

    time.sleep(random.uniform(2,4))

# -------------------------
# Step 5 — Convert to DataFrame
# -------------------------
df = pd.DataFrame(all_series)
df.to_csv("market_trends.csv")

# -------------------------
# Step 6 — Growth scoring
# -------------------------
growth = {}

for col in df.columns:
    first = df[col].head(10).mean()
    last = df[col].tail(10).mean()
    if first == 0:
        growth[col] = last
    else:
        growth[col] = round(((last - first) / first) * 100, 2)

growth_df = pd.DataFrame(growth.items(), columns=["Keyword", "Growth %"])
growth_df = growth_df.sort_values("Growth %", ascending=False)
growth_df.to_csv("trend_growth.csv", index=False)

print("\nTop Opportunities:")
print(growth_df)
