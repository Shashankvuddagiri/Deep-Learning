import os
import uuid
from gtts import gTTS
from typing import Optional
import aiofiles

class AudioService:
    def __init__(self):
        self.audio_dir = "static/audio"
        os.makedirs(self.audio_dir, exist_ok=True)
    
    async def generate_audio(self, text: str, language: str = "en") -> Optional[str]:
        """
        Generate audio file from text using gTTS
        """
        try:
            if not text or len(text.strip()) == 0:
                return None
            
            # Limit text length for audio generation
            max_length = 500
            if len(text) > max_length:
                text = text[:max_length] + "..."
            
            # Generate unique filename
            audio_id = str(uuid.uuid4())
            filename = f"{audio_id}.mp3"
            filepath = os.path.join(self.audio_dir, filename)
            
            # Generate audio
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(filepath)
            
            # Return URL path
            return f"/static/audio/{filename}"
            
        except Exception as e:
            print(f"Error generating audio: {e}")
            return None
    
    async def generate_landmark_audio(self, landmark_name: str, summary: str) -> Optional[str]:
        """
        Generate audio specifically for landmark information
        """
        try:
            # Create a more engaging text for audio
            audio_text = f"Welcome to {landmark_name}. {summary}"
            
            return await self.generate_audio(audio_text)
            
        except Exception as e:
            print(f"Error generating landmark audio: {e}")
            return None
    
    def cleanup_old_audio(self, max_age_hours: int = 24):
        """
        Clean up old audio files to save storage
        """
        try:
            import time
            current_time = time.time()
            max_age_seconds = max_age_hours * 3600
            
            for filename in os.listdir(self.audio_dir):
                if filename.endswith('.mp3'):
                    filepath = os.path.join(self.audio_dir, filename)
                    file_age = current_time - os.path.getmtime(filepath)
                    
                    if file_age > max_age_seconds:
                        os.remove(filepath)
                        print(f"Deleted old audio file: {filename}")
                        
        except Exception as e:
            print(f"Error cleaning up audio files: {e}")
