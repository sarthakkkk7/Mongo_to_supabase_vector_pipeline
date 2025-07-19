def run():
    print("Running Step 1: MongoDB Insertion")

import json
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
print("Connecting to MongoDB...")
client = MongoClient(MONGO_URI)
db = client["candidate_db"]
collection = db["candidates"]

# Load JSON data
with open("candidates-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert $oid to ObjectId
for item in data:
    if "_id" in item and "$oid" in item["_id"]:
        item["_id"] = ObjectId(item["_id"]["$oid"])

# Insert into MongoDB
try:
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} records successfully.")
except Exception as e:
    print(f"Error inserting data: {e}")
