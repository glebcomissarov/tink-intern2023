import requests
import ujson
import pandas as pd
from io import StringIO


resp = requests.get(
    "http://127.0.0.1:8000/get_purchases?date=2023-03-20&bank_name=tinkoff"
)
print(resp.json())
