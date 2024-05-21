import os
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from fastapi.middleware.cors import CORSMiddleware
from src import inference

# Initialize Global Variables
load_dotenv(find_dotenv())
open_api_key = os.getenv("OPEN_API_KEY")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(inference.router)