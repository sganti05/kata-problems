import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_article(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
            {"role": "user", "content": f"Summarize this article:\n\n{content}"}
        ],
        max_tokens = 300,
        temperature = 0.5,
    )
    return response.choices[0].message.content