# ChronoScope – Turning Images into Timelines

🧠 An intelligent historical image detection and storytelling platform that recognizes historical landmarks or artifacts from images and presents interactive stories with text, audio, and animated avatars.

## Features

- **Image Recognition**: CNN/ViT + CLIP for historical landmark detection
- **Knowledge Retrieval**: Wikipedia/Wikidata integration for verified historical information
- **AI Storytelling**: NLP + TTS for narrative summaries
- **Interactive Presentation**: Text, audio, and optional animated avatars
- **Explore Page**: Curated monuments discovery
- **Feedback System**: User corrections and improvements

## Tech Stack

### Frontend
- React.js (Vite)
- Tailwind CSS
- Shadcn UI
- Axios
- React Router

### Backend
- Python (FastAPI)
- PyTorch (CLIP/ViT)
- Hugging Face Transformers
- FAISS
- gTTS
- SQLite
- Wikipedia API

## Quick Start

1. **Install Dependencies**
   ```bash
   npm install
   npm run frontend:install
   npm run backend:install
   ```

2. **Start Development Servers**
   ```bash
   npm run dev
   ```

3. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Project Structure

```
ChronoScope/
├── frontend/          # React.js frontend
├── backend/           # FastAPI backend
├── package.json       # Root package configuration
└── README.md          # This file
```

## API Endpoints

- `POST /api/v1/identify` - Image recognition
- `GET /api/v1/explore` - Curated monuments
- `POST /api/v1/feedback` - User feedback
- `GET /api/v1/history` - Recent predictions

## Development

The project uses concurrently to run both frontend and backend simultaneously during development.
