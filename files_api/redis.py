import aioredis
import os


class Redis:
    def __init__(self):
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        self.client = aioredis.from_url(redis_url)

    def insert(self, key, data, expire=None):
        await self.client.set(name=key, value=data, keepttl=expire)

    def retrieve(self, key):
        return await self.client.get(name=key)
