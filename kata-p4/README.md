News Summarization Tool using LLMs:

This project is a command-line Python application that summarizes news articles using a Large Language Model (LLM) via the OpenAI API. It extracts content from a given news URL, generates a concise summary, and stores the result in JSON format.

Features:

- Extracts article content from URLs using `newspaper3k`
- Summarizes using OpenAI's `gpt-3.5-turbo` model
- Stores results with date, summary, and article type
- Optional Q&A interface to interact with saved summaries

How to Run:

1. Install dependencies:
bash
pip install openai newspaper3k beautifulsoup4 requests

2. Set your OpenAI API key:

On PowerShell:
$env:OPENAI_API_KEY="your-api-key"

On CMD:
set OPENAI_API_KEY=your-api-key

3. Run the program:
python main.py


Example Output (data.json):

{
  "date": "25 June 2025",
  "summary": "The article discusses the increasing popularity of AI-driven solutions in journalism...",
  "articleType": "technology"
}