from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

item_master = { 1 : "This is a Mango.",
                2 : "This is an Apple.",
                3 : "This is a Banana.",
                4 : "This is an Orange.",
                5 : "This is a Pear.", 
                }

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {" message": "Hello World"}

@app.get("/items")
async def items():
    return { "items" : item_master }

@app.get("/items/{item_id}")
async def get_item(item_id: int,short: bool = False):
    if short == True: 
        return {"item" : item_master[item_id]}
    else:
        return {"item" : "This is a long description"}
   
@app.post("/items")
async def create_item(item:Item):
    return item

