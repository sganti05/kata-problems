import json
from datetime import datetime
from extractor import extract_article
from summarizer import summarize_article

def create_entry(url, article_type):
    content = extract_article(url)
    summary = summarize_article(content)
    entry = {
        "date": datetime.today().strftime("%d %B %Y"),
        "summary": summary,
        "articleType": article_type
    }
    return entry

def save_entry(entry, filename="data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    url = input("Enter news article URL: ")
    article_type = input("Enter article type (e.g., political, financial, tech): ")
    entry = create_entry(url, article_type)
    save_entry(entry)
    print("Summary saved to data.json!")