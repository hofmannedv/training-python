# SPDX-FileCopyrightText: 2021 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

# FastAPI example with get, and put requests
# Taken from Python für Data Science Tutorial:
# https://www.python4data.science/de/latest/data-processing/apis/fastapi/install.html

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
