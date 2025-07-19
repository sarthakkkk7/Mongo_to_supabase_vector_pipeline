# 🚀 MongoDB to Supabase Vector Pipeline

This project is a full-fledged data pipeline that takes structured candidate data in JSON format, stores it in MongoDB, transforms it into a flattened readable text string, generates vector embeddings using a Sentence Transformer, and finally stores everything into a pgvector-enabled PostgreSQL database hosted on Supabase. The best part? It’s fully duplicate-safe.

---

## 🧠 Pipeline Overview

1. 📥 **Insert into MongoDB**  
   Raw JSON data is inserted into a MongoDB collection.

2. 🧹 **Flatten & Embed**  
   Candidate profiles are transformed into a single text block and embedded using `all-MiniLM-L6-v2`.

3. 🛢 **Insert into Supabase PostgreSQL**  
   Content and vector embeddings are stored in a `candidates` table with pgvector support.

4. 🔁 **Avoid Duplicate Uploads**  
   Already-uploaded records (based on `mongo_id`) are skipped on reruns.

---

## 💼 Ideal Use Cases

- Resume Matching & Candidate Search
- Vector-Based Semantic Retrieval Systems
- LLM Data Indexing Pipelines
- Generative AI applications for HR tech

---

## 🧰 Tech Stack

- Python
- MongoDB (Atlas or local)
- Supabase PostgreSQL + pgvector
- Sentence Transformers
- SQLAlchemy
- Psycopg2
- tqdm, dotenv

---

## 🛠️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mongo-to-supabase-pipeline.git
cd mongo-to-supabase-pipeline
```

### 2. Create `.env` File

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
SUPABASE_URL=postgresql+psycopg2://<user>:<password>@<host>.supabase.co:5432/<database>
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

```bash
python step1_insert_to_mongo.py
python step2_generate_embeddings.py
python step3_insert_to_supabase.py
```

---

## 🗃️ Supabase Table Schema

| Column     | Type    | Description                          |
|------------|---------|--------------------------------------|
| id         | SERIAL  | Primary key                          |
| mongo_id   | TEXT    | Unique identifier from MongoDB       |
| content    | TEXT    | Flattened profile text               |
| embedding  | VECTOR  | Vector embedding of the content      |

---

## 🧾 Example File Structure

```
mongo_to_supabase_pipeline/
├── candidates-data.json
├── output_for_supabase.json
├── .env
├── step1_insert_to_mongo.py
├── step2_generate_embeddings.py
├── step3_insert_to_supabase.py
├── requirements.txt
└── README.md
```

---

## 🔥 What Makes This Cool

- ✅ Modular and readable Python structure
- ✅ Easy integration with AI search systems
- ✅ Works seamlessly with Supabase + pgvector
- ✅ Avoids duplicate uploads using `mongo_id`
- ✅ Ready for extension with search APIs or LLMs

---

## 👨‍💻 Author

**Sarthak Satish Deshmukh**   
[GitHub](https://github.com/sarthakkkk7) • [LinkedIn](https://www.linkedin.com/in/sarthakkkk7)


---

## 📄 License

MIT License – Feel free to use, modify, and build upon this project.
