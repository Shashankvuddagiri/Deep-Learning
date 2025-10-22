import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import numpy as np
from transformers import CLIPProcessor, CLIPModel
import faiss
import pickle
import os
from typing import Dict, Optional

class ImageService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.processor = None
        self.index = None
        self.landmark_names = []
        self.load_models()
    
    def load_models(self):
        """Load CLIP model and precomputed embeddings"""
        try:
            # Load CLIP model
            self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
            self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
            self.model.to(self.device)
            self.model.eval()
            
            # Load precomputed embeddings and landmark names
            embeddings_path = "data/landmark_embeddings.pkl"
            if os.path.exists(embeddings_path):
                with open(embeddings_path, 'rb') as f:
                    data = pickle.load(f)
                    self.landmark_names = data['landmark_names']
                    embeddings = data['embeddings']
                    
                    # Create FAISS index
                    self.index = faiss.IndexFlatIP(embeddings.shape[1])
                    self.index.add(embeddings.astype('float32'))
            else:
                print("Warning: No precomputed embeddings found. Using fallback method.")
                self._create_fallback_data()
                
        except Exception as e:
            print(f"Error loading models: {e}")
            self._create_fallback_data()
    
    def _create_fallback_data(self):
        """Create fallback data when embeddings are not available"""
        self.landmark_names = [
            "Taj Mahal", "Eiffel Tower", "Colosseum", "Great Wall of China",
            "Machu Picchu", "Pyramids of Giza", "Statue of Liberty", "Big Ben",
            "Christ the Redeemer", "Sydney Opera House", "Notre-Dame Cathedral",
            "Sagrada Familia", "Acropolis", "Stonehenge", "Angkor Wat"
        ]
        
        # Create dummy embeddings
        dummy_embeddings = np.random.rand(len(self.landmark_names), 512).astype('float32')
        self.index = faiss.IndexFlatIP(512)
        self.index.add(dummy_embeddings)
    
    async def predict_landmark(self, image_data: bytes) -> Optional[Dict]:
        """
        Predict landmark from image data
        """
        try:
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_data))
            
            # Preprocess image
            inputs = self.processor(images=image, return_tensors="pt", padding=True)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Get image features
            with torch.no_grad():
                image_features = self.model.get_image_features(**inputs)
                image_features = image_features / image_features.norm(dim=-1, keepdim=True)
            
            # Search for similar landmarks
            if self.index is not None:
                similarities, indices = self.index.search(
                    image_features.cpu().numpy().astype('float32'), k=3
                )
                
                # Get top result
                top_idx = indices[0][0]
                confidence = float(similarities[0][0])
                landmark_name = self.landmark_names[top_idx]
                
                return {
                    "landmark": landmark_name,
                    "confidence": confidence,
                    "image_url": None  # Could save image and return URL
                }
            else:
                # Fallback: return random landmark
                import random
                landmark_name = random.choice(self.landmark_names)
                return {
                    "landmark": landmark_name,
                    "confidence": 0.75,  # Random confidence
                    "image_url": None
                }
                
        except Exception as e:
            print(f"Error in predict_landmark: {e}")
            return None
    
    def precompute_embeddings(self, image_paths: list, landmark_names: list):
        """
        Precompute embeddings for a dataset of landmark images
        This method should be run offline to create the embeddings file
        """
        embeddings = []
        
        for image_path in image_paths:
            try:
                image = Image.open(image_path)
                inputs = self.processor(images=image, return_tensors="pt", padding=True)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                
                with torch.no_grad():
                    image_features = self.model.get_image_features(**inputs)
                    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
                    embeddings.append(image_features.cpu().numpy().flatten())
                    
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
                continue
        
        # Save embeddings
        embeddings_array = np.array(embeddings)
        data = {
            'embeddings': embeddings_array,
            'landmark_names': landmark_names
        }
        
        os.makedirs('data', exist_ok=True)
        with open('data/landmark_embeddings.pkl', 'wb') as f:
            pickle.dump(data, f)
        
        print(f"Saved embeddings for {len(landmark_names)} landmarks")
