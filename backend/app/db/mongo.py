import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

client: Optional[AsyncIOMotorClient] = None
db = None

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "faq_chatbot")


async def connect_db():
    global client, db
    try:
        client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        # Ping to verify connection
        await client.admin.command("ping")
        db = client[DB_NAME]
        print(f"✓ Connected to MongoDB at {MONGO_URL}")
    except Exception as e:
        print(f"⚠️  MongoDB not available: {e}")
        print("⚠️  App will run without persistence (chat history won't be saved)")
        db = None


async def close_db():
    global client
    if client:
        client.close()
        print("✓ MongoDB connection closed")


def get_db():
    return db