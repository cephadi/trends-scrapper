# 📈 Market Trend Scraper  
*(Google Trends Edition)*

This project is a simple Python script that collects **emerging market trends** from **[Google Trends](https://trends.google.com/trends)** and exports them into a CSV file for further analysis.

---

## 🎯 What This Script Does

The script:
- Scrapes trending topics from **https://trends.google.com/**
- Extracts:
  - Topic name  
  - Growth indicator  
  - Category  
- Saves the data into a CSV file:  
  `market_trends.csv`

You can use this data for:
- Finding new business ideas  
- Market demand analysis  
- Trend tracking  
- Research dashboards  

---

## 📦 Requirements

You need Python 3.8+ and the following libraries:

```bash
pip install -r requirements.txt
````

---

## ▶️ How to Run

```bash
python3 trend_scraper.py
```

3. After it finishes, you will get:

```
market_trends.csv
```

Open it with Excel, Google Sheets, or any data analysis tool.

---

## 📁 Output Example

The CSV file will look like this:

| topic          | growth | category   |
| -------------- | ------ | ---------- |
| AI Avatar      | +480%  | Technology |
| Portable Sauna | +320%  | Health     |
| Smart Rings    | +210%  | Wearables  |

*(Actual values depend on current trends.)*

## ⚠️ Notes

* This script scrapes **publicly available data**.
* Website structure may change, requiring selector updates.
* Use responsibly and respect the website’s terms.

---

## 🚀 Next Steps

You can extend this by:

* Running it on a schedule (daily/weekly)
* Tracking historical growth
* Combining with Product Hunt, Amazon, or Reddit trend data

This turns it from a script into a **real market intelligence tool**.