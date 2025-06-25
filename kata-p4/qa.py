import json

def ask_questions():
    with open("data.json") as f:
        data = json.load(f)

    print("You can ask things like:\n- What are all article types?\n- Show all financial summaries.")
    question = input("Ask a question: ").lower()

    if "article types" in question:
        types = {item['articleType'] for item in data}
        print("Types:", types)
    elif "financial" in question:
        for item in data:
            if item['articleType'].lower() == "financial":
                print(f"[{item['date']}] {item['summary']}\n")

if __name__ == "__main__":
    ask_questions()

