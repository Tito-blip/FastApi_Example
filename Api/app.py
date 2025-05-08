from fastapi import FastAPI
import json

with open('items.json') as file:
    data = json.load(file)
    

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Hello World"}

@app.get("/items")
def get_items():
    return {"items": data}

@app.get("/item/{item_id}")
def list_item_id(item_id: int):
    for item in data:
        if item['id'] == item_id:
            return item
    return {"Error"}

