from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from src.core.router import router

app = FastAPI(title="Demo")

app.include_router(router)



# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items/")
# def create_item(item: Item):
#     return item


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
# @app.get("/elems/")
# def read_elem(item_id: int = 1, name: str = None):
#     return {"item_id": item_id, "name": name}
#
# @app.get("/elems/{elem_id}")
# def read_elem(item_id: int = 1, name: str = None, description: str = None):
#     return {"item_id": item_id, "name": name, "description": description}