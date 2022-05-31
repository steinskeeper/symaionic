from fastapi import FastAPI
from api.path import path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(path)



@app.get("/")
async def root():
    type = "hello"
    return {"message": "Hello World",
            "type": type}
