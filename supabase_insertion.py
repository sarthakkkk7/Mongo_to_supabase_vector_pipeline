def run():
    print("Running Step 3: Supabase Insertion")

import os
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from pgvector.sqlalchemy import Vector

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")  

# Create DB engine
engine = create_engine(SUPABASE_URL)

# Load our output file from Step 2
with open("output_for_supabase.json", "r", encoding="utf-8") as f:
    records = json.load(f)

print("Fetching existing mongo_ids to avoid duplicates...")
with engine.begin() as conn:
    result = conn.execute(text("SELECT mongo_id FROM candidates"))
    existing_ids = {row[0] for row in result.fetchall()}

print(f"Found {len(existing_ids)} existing records.")
print("Inserting into Supabase (skipping duplicates)...")

inserted_count = 0
with engine.begin() as conn:
    for rec in records:
        mongo_id = rec["mongo_id"]
        if mongo_id in existing_ids:
            print(f"Skipping duplicate mongo_id: {mongo_id}")
            continue

        query = text("""
            INSERT INTO candidates (mongo_id, content, embedding)
            VALUES (:mongo_id, :content, :embedding)
        """)
        conn.execute(query, {
            "mongo_id": mongo_id,
            "content": rec["content"],
            "embedding": rec["embedding"]
        })
        inserted_count += 1

print(f"Uploaded {inserted_count} new records to Supabase PostgreSQL (Skipped {len(records) - inserted_count} duplicates).")
