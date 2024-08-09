import motor.motor_asyncio
import asyncio
from config import Config


class MongoDBHelper:

    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)
        self.db = self.client.get_database(Config.MONGODB_NAME)
        self.collection = self.db.get_collection(Config.MONGODB_COLLECTION)

    async def get_all_users(self):
        users_cursor = self.collection.find()
        users_list = await users_cursor.to_list(length=1)
        return users_list


if __name__ == "__main__":
    Config.initialize()

    async def fetch_users():
        mongo_helper = MongoDBHelper()
        users = await mongo_helper.get_all_users()
        print(users)

    asyncio.run(fetch_users())
