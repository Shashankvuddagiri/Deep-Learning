#!/usr/bin/env python3
"""
ChronoScope Backend Startup Script
"""
import uvicorn
import os
import sys

if __name__ == "__main__":
    # Set environment variables
    os.environ.setdefault("DATABASE_URL", "sqlite:///./chronoscope.db")
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
