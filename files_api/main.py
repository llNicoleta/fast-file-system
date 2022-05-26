import aiohttp
import uvicorn
from fastapi import FastAPI, UploadFile
from db import TestDatabase
from redis import Redis


app = FastAPI()
db = TestDatabase()
redis = Redis()


@app.post("/scan-file")
async def add_file(file: UploadFile):
    async with aiohttp.ClientSession() as session:
        async with session.post(
                'https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/',
                data={'file': await file.read()}) as resp:
            res = await resp.json()
            await redis.insert(res['hash'], res['risk_level'], 600)
            await db.insert_data(res)
            return res

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
