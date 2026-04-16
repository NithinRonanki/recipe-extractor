from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .scraper import extract_recipe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str


@app.get("/")
def read_root():
    return {"message": "API is working 🚀"}


@app.post("/extract")
def extract(data: URLRequest):
    return extract_recipe(data.url)
