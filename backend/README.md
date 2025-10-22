# ChronoScope Backend

FastAPI backend for the ChronoScope historical image detection platform.

## Features

- **Image Recognition**: CLIP and ViT models for landmark detection
- **Wikipedia Integration**: Automatic historical information retrieval
- **Audio Generation**: Text-to-speech using gTTS
- **Database**: SQLite with SQLAlchemy for storing predictions and feedback
- **REST API**: Complete REST API with CORS support

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python run.py
```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /api/v1/identify` - Image landmark identification
- `GET /api/v1/explore` - Curated monuments
- `GET /api/v1/history` - Prediction history
- `DELETE /api/v1/history/{id}` - Delete prediction
- `POST /api/v1/feedback` - Submit feedback

## Configuration

Set environment variables:
- `DATABASE_URL`: Database connection string
- `API_HOST`: Host to bind to (default: 0.0.0.0)
- `API_PORT`: Port to bind to (default: 8000)

## Development

The application will automatically reload when files change in development mode.
