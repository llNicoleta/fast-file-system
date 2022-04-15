import aiohttp
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/scan-file")
async def add_file(file: UploadFile):
    async with aiohttp.ClientSession() as session:
        async with session.post(
                'https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/',
                data={'file': await file.read()}) as resp:
            res = await resp.json()
            return res

