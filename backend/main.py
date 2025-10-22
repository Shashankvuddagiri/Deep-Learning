from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import uvicorn
import os
from datetime import datetime
import uuid

from database import get_db, engine, Base
from models import Prediction, Feedback
from services.image_service import ImageService
from services.wikipedia_service import WikipediaService
from services.audio_service import AudioService
from services.explore_service import ExploreService

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ChronoScope API",
    description="Historical Image Detection and Storytelling Platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize services
image_service = ImageService()
wikipedia_service = WikipediaService()
audio_service = AudioService()
explore_service = ExploreService()

@app.get("/")
async def root():
    return {"message": "ChronoScope API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/v1/identify")
async def identify_image(
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Identify historical landmark in uploaded image
    """
    try:
        # Validate image file
        if not image.content_type or not image.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read image data
        image_data = await image.read()
        
        # Process image with AI models
        prediction_result = await image_service.predict_landmark(image_data)
        
        if not prediction_result:
            raise HTTPException(status_code=400, detail="Could not identify landmark in image")
        
        # Get Wikipedia information
        wikipedia_info = await wikipedia_service.get_landmark_info(prediction_result['landmark'])
        
        # Generate audio narration
        audio_url = None
        if wikipedia_info.get('summary'):
            audio_url = await audio_service.generate_audio(wikipedia_info['summary'])
        
        # Save prediction to database
        prediction = Prediction(
            id=str(uuid.uuid4()),
            filename=image.filename or "unknown",
            landmark=prediction_result['landmark'],
            confidence=prediction_result['confidence'],
            summary=wikipedia_info.get('summary', ''),
            year_built=wikipedia_info.get('year_built'),
            location=wikipedia_info.get('location'),
            image_url=prediction_result.get('image_url'),
            audio_url=audio_url,
            reference_url=wikipedia_info.get('reference_url'),
            timestamp=datetime.utcnow()
        )
        
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        
        # Return response
        return {
            "landmark": prediction_result['landmark'],
            "confidence": prediction_result['confidence'],
            "summary": wikipedia_info.get('summary', ''),
            "year_built": wikipedia_info.get('year_built'),
            "location": wikipedia_info.get('location'),
            "image_url": prediction_result.get('image_url'),
            "audio_url": audio_url,
            "reference_url": wikipedia_info.get('reference_url')
        }
        
    except Exception as e:
        print(f"Error in identify_image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/v1/explore")
async def get_explore_monuments():
    """
    Get curated monuments for explore page
    """
    try:
        monuments = await explore_service.get_curated_monuments()
        return monuments
    except Exception as e:
        print(f"Error in get_explore_monuments: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/v1/history")
async def get_prediction_history(db: Session = Depends(get_db)):
    """
    Get recent prediction history
    """
    try:
        predictions = db.query(Prediction).order_by(Prediction.timestamp.desc()).limit(50).all()
        return [
            {
                "id": pred.id,
                "filename": pred.filename,
                "landmark": pred.landmark,
                "confidence": pred.confidence,
                "timestamp": pred.timestamp.isoformat(),
                "image_url": pred.image_url
            }
            for pred in predictions
        ]
    except Exception as e:
        print(f"Error in get_prediction_history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.delete("/api/v1/history/{prediction_id}")
async def delete_prediction(prediction_id: str, db: Session = Depends(get_db)):
    """
    Delete a prediction from history
    """
    try:
        prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
        if not prediction:
            raise HTTPException(status_code=404, detail="Prediction not found")
        
        db.delete(prediction)
        db.commit()
        
        return {"message": "Prediction deleted successfully"}
    except Exception as e:
        print(f"Error in delete_prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/api/v1/feedback")
async def submit_feedback(
    image_id: str,
    predicted_qid: str,
    correct_qid: str = None,
    comment: str = None,
    db: Session = Depends(get_db)
):
    """
    Submit feedback for prediction accuracy
    """
    try:
        feedback = Feedback(
            id=str(uuid.uuid4()),
            image_id=image_id,
            predicted_qid=predicted_qid,
            correct_qid=correct_qid,
            comment=comment,
            timestamp=datetime.utcnow()
        )
        
        db.add(feedback)
        db.commit()
        db.refresh(feedback)
        
        return {"message": "Feedback submitted successfully"}
    except Exception as e:
        print(f"Error in submit_feedback: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
