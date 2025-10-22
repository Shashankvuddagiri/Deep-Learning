from sqlalchemy import Column, String, Float, DateTime, Text
from sqlalchemy.dialects.sqlite import UUID
from database import Base
from datetime import datetime

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(String, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    landmark = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    summary = Column(Text)
    year_built = Column(String)
    location = Column(String)
    image_url = Column(String)
    audio_url = Column(String)
    reference_url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"
    
    id = Column(String, primary_key=True, index=True)
    image_id = Column(String, nullable=False)
    predicted_qid = Column(String, nullable=False)
    correct_qid = Column(String)
    comment = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
