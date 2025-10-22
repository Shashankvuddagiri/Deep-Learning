import requests
import re
from typing import Dict, Optional
from datetime import datetime

class WikipediaService:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/api/rest_v1"
        self.sparql_url = "https://query.wikidata.org/sparql"
    
    async def get_landmark_info(self, landmark_name: str) -> Dict:
        """
        Get comprehensive information about a landmark from Wikipedia and Wikidata
        """
        try:
            # Get Wikipedia summary
            wiki_info = await self._get_wikipedia_summary(landmark_name)
            
            # Get Wikidata information
            wikidata_info = await self._get_wikidata_info(landmark_name)
            
            # Combine information
            result = {
                "summary": wiki_info.get("summary", ""),
                "reference_url": wiki_info.get("reference_url", ""),
                "year_built": wikidata_info.get("year_built"),
                "location": wikidata_info.get("location"),
                "image_url": wiki_info.get("image_url")
            }
            
            return result
            
        except Exception as e:
            print(f"Error getting landmark info for {landmark_name}: {e}")
            return {
                "summary": f"Information about {landmark_name} is not available at the moment.",
                "reference_url": "",
                "year_built": None,
                "location": None,
                "image_url": None
            }
    
    async def _get_wikipedia_summary(self, landmark_name: str) -> Dict:
        """
        Get summary from Wikipedia REST API
        """
        try:
            # Clean landmark name for URL
            clean_name = landmark_name.replace(" ", "_")
            
            # Get page summary
            url = f"{self.base_url}/page/summary/{clean_name}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "summary": data.get("extract", ""),
                    "reference_url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
                    "image_url": data.get("thumbnail", {}).get("source") if data.get("thumbnail") else None
                }
            else:
                return {"summary": "", "reference_url": "", "image_url": None}
                
        except Exception as e:
            print(f"Error getting Wikipedia summary: {e}")
            return {"summary": "", "reference_url": "", "image_url": None}
    
    async def _get_wikidata_info(self, landmark_name: str) -> Dict:
        """
        Get structured data from Wikidata
        """
        try:
            # This is a simplified version - in practice, you'd use SPARQL queries
            # to get structured data from Wikidata
            
            # For now, return some mock data based on common landmarks
            landmark_data = {
                "Taj Mahal": {
                    "year_built": "1632-1653",
                    "location": "Agra, India"
                },
                "Eiffel Tower": {
                    "year_built": "1887-1889",
                    "location": "Paris, France"
                },
                "Colosseum": {
                    "year_built": "70-80 AD",
                    "location": "Rome, Italy"
                },
                "Great Wall of China": {
                    "year_built": "7th century BC - 17th century AD",
                    "location": "China"
                },
                "Machu Picchu": {
                    "year_built": "1450",
                    "location": "Cusco Region, Peru"
                },
                "Pyramids of Giza": {
                    "year_built": "2580-2510 BC",
                    "location": "Giza, Egypt"
                },
                "Statue of Liberty": {
                    "year_built": "1886",
                    "location": "New York, USA"
                },
                "Big Ben": {
                    "year_built": "1859",
                    "location": "London, UK"
                },
                "Christ the Redeemer": {
                    "year_built": "1922-1931",
                    "location": "Rio de Janeiro, Brazil"
                },
                "Sydney Opera House": {
                    "year_built": "1959-1973",
                    "location": "Sydney, Australia"
                }
            }
            
            return landmark_data.get(landmark_name, {
                "year_built": None,
                "location": None
            })
            
        except Exception as e:
            print(f"Error getting Wikidata info: {e}")
            return {"year_built": None, "location": None}
    
    def _extract_year_from_text(self, text: str) -> Optional[str]:
        """
        Extract year information from text using regex
        """
        # Look for 4-digit years
        years = re.findall(r'\b(1[0-9]{3}|2[0-9]{3})\b', text)
        if years:
            return years[0]
        return None
