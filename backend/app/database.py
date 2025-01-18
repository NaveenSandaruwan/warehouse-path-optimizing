from pymongo import MongoClient
from .config import MONGO_URI, DATABASE_NAME

# Initialize MongoDB connection
def connect_to_mongodb():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        print("Connected to MongoDB successfully!")
        return db
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None

# Connect to the database
db = connect_to_mongodb()

assets_collection = db["assets"] if db is not None else None

if assets_collection:
    assets_collection.create_index("_id", unique=True)