from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from io import StringIO
from datetime import datetime
import ujson
from test_api.api.utils import get_json

app = FastAPI(
    title="Рога и копыта API",
    description="часть API маркетплейса 'Рога и Копыта'",
    version="1.21.0",
)


class Product(BaseModel):
    purchase_id: int
    purchase_date: str
    bank_id: int
    category_id: int
    product_id: int
    product_price: float

    class Config:
        schema_extra = {
            "example": {
                "purchase_id": 1250007534,
                "purchase_date": "2023-02-21 10:00:00.000",
                "bank_id": 1,
                "category_id": 10,
                "product_id": 207,
                "product_price": 1205.20,
            }
        }


class Purchases(BaseModel):
    response: list[Product]


@app.get("/get_purchases")
def get_purchases(date: str, bank_name: str) -> Purchases:
    """
    Return a json object that contains
    an array of purchares that were made
    using the cards of the specified bank
    """

    response_str = StringIO()
    response_str.write('{"response": ')
    response_str.write(get_json())
    response_str.write("}")
    print(response_str.getvalue())
    return ujson.loads(response_str.getvalue())
