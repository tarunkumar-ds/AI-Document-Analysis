from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.pdf.extractor import extract_text
from app.nlp.cleaner import clean_text
from app.nlp.summarizer import summarize
from app.nlp.keywords import extract_keywords
from app.nlp.sentiment import analyze_sentiment
app = FastAPI(title="Document Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...)):

    try:
        
        raw_text = extract_text(file.file)

        if not raw_text:
            return {
                "status": "failed",
                "message": "No readable text found",
                "note": "Scanned PDFs need OCR"
            }
        
        cleaned_text = clean_text(raw_text)
        
        summary = summarize(cleaned_text)
        keywords = extract_keywords(cleaned_text)
        sentiment = analyze_sentiment(cleaned_text)

        return {
            "status": "success",
            "summary": summary,
            "keywords": keywords,
            "sentiment": sentiment
        }

    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }
