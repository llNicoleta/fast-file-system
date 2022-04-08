from typing import Optional

import uvicorn
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from pydantic.class_validators import validator
import aiohttp


app = FastAPI()


class ItemModel(BaseModel):
    name: str
    description: str
    price: int
    image: Optional[str]

    @validator('price')
    def price_not_zero(cls, price):
        if price == 0:
            raise ValueError("Price shouldn't be zero")
        return price


@app.post("/some-json")
async def add_item(item: ItemModel) -> ItemModel:
    return item


@app.post("/some_file")
async def add_file(file: UploadFile):
    async with aiohttp.ClientSession() as session:
        async with session.post(
                'https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/',
                data={'file': await file.read()}) as resp:
            res = await resp.json()
            return res


if __name__ == '__main__':
    uvicorn.run(app)
