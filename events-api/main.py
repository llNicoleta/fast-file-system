from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, validator

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


@app.get("/")
async def root():
    return {'title': 'Fast File System'}


@app.post("/scan-file")
async def add_item(item: ItemModel) -> ItemModel:
    return item


if __name__ == '__main__':
    uvicorn.run(app)