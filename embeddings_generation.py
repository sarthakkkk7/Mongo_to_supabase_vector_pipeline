def run():
    print("Running Step 2: Embeddings Generation")

from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from sentence_transformers import SentenceTransformer
import os
import json

# Load env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["candidate_db"]
collection = db["candidates"]

# Load Sentence Transformer model
print("Loading Sentence Transformer model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to stringify each MongoDB document
def stringify_doc(doc):
    doc.pop("_id", None)  # We'll keep _id separately
    return json.dumps(doc, ensure_ascii=False)

# Fetch data from Mongo
print("Fetching data from MongoDB...")
all_docs = list(collection.find({}))

data_for_supabase = []

for doc in all_docs:
    mongo_id = str(doc["_id"])
    stringified = stringify_doc(doc)
    embedding = model.encode(stringified).tolist()
    data_for_supabase.append({
        "mongo_id": mongo_id,
        "content": stringified,
        "embedding": embedding
    })

# Save output to a local JSON file for inspection or step 3
with open("output_for_supabase.json", "w", encoding="utf-8") as f:
    json.dump(data_for_supabase, f, ensure_ascii=False, indent=2)

print(f"Generated embeddings for {len(data_for_supabase)} candidates.")
