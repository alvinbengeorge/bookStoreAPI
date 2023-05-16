from fastapi import FastAPI, Response
from routes import read, create, update, delete
from json import dumps

app = FastAPI()
app.include_router(read.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)

@app.get("/")
async def home():
    return Response(
        dumps({"message": "Welcome to BookStoreAPI"}),
        status_code=200,
        media_type="application/json"
    )

