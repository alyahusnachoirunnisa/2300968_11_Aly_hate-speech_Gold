from fastapi import APIRouter
from fastapi import Query
from fastapi import File,UploadFile
from services.sentiment import get_sentiment, get_sentiment_file
import pandas as pd


router = APIRouter()

@router.get("/sentiment")
async def text_sentiment(sentence:str = Query(default="")):
    
    result = await get_sentiment(sentence)

    return result

import io
@router.post("/sentiment-upload")
async def upload_file(file : UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    result = await get_sentiment_file(df)
    return result