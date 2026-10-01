from fastapi import FastAPI 
from app.routes import issues
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timer_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(issues.router)












#             TESTING
# items = [
#     {"id": 1, "name": "MR.P"},
#     {"id": 2, "name": "MR.D"},
#     {"id": 3, "name": "MR.A"},
# ]
# # Creating routes
# @app.get("/health")  
# def health_check():
#     return{"status": "ok"}

# @app.get("/item")
# def get_items():
#     return items 

# @app.get("/item/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     else:
#             return("Item not Found")
    

# @app.post("/item") 
# def create_item (item: dict):
#      items.append(item)
#      return item 