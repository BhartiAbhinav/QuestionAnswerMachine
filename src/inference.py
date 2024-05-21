from fastapi import APIRouter, Form, UploadFile
from pydantic import BaseModel

router = APIRouter()


@router.post("/predict")
async def predict(query: Form(...), file: UploadFile):
    pass
