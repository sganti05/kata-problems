import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os

df = pd.read_csv("movies.csv")

chroma_client = chromadb.Client()

openai_embedder = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-ada-002"
)

collection = chroma_client.get_or_create_collection(
    name="movies",
    embedding_function=openai_embedder
)

print("Connected to ChromaDB and ready to store vectors.")

for idx, row in df.iterrows():
    if pd.isna(row['Description']) or row['Description'].strip() == "":
        continue

    movie_id = f"movie-{idx}"
    document = row["Description"]
    metadata = {
        "Title": row['Title'],
        "Genre": row['Genre'],
        "Director": row['Director']

    }

    collection.add(
        documents=[document],
        metadatas=[metadata],
        ids=[movie_id]
    )

print("All movie descriptions embedded and stored in ChromaDB.")

user_query = input("\n What kind of movie are you looking for? ")
results = collection.query(
    query_texts=[user_query],
    n_results=5
)

print("\n Top 5 Recommended Movies:\n")
for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"- {meta['Title']} ({meta['Genre']}) - Directed by {meta['Director']}")
