import os
from pymongo import MongoClient
from dotenv import load_dotenv
import gridfs

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path, override=True)

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("ERROR: MONGO_URI was not found in .env")
    exit()

print("Mongo URI loaded successfully")

try:
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")

    db = client["ai_project"]
    fs = gridfs.GridFS(db)

    print("MongoDB Atlas connection successful!")

except Exception as e:
    print("MongoDB connection failed!")
    print(e)