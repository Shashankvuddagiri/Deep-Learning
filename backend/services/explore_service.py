from typing import List, Dict
import random

class ExploreService:
    def __init__(self):
        self.curated_monuments = [
            {
                "id": "taj-mahal",
                "title": "Taj Mahal",
                "image": "https://images.unsplash.com/photo-1564507592333-c6065ee702c3?w=800",
                "short_text": "An ivory-white marble mausoleum in Agra, India, built by Mughal emperor Shah Jahan in memory of his wife Mumtaz Mahal.",
                "year_built": "1632-1653",
                "location": "Agra, India",
                "reference_url": "https://en.wikipedia.org/wiki/Taj_Mahal"
            },
            {
                "id": "eiffel-tower",
                "title": "Eiffel Tower",
                "image": "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?w=800",
                "short_text": "A wrought-iron lattice tower on the Champ de Mars in Paris, France, named after engineer Gustave Eiffel.",
                "year_built": "1887-1889",
                "location": "Paris, France",
                "reference_url": "https://en.wikipedia.org/wiki/Eiffel_Tower"
            },
            {
                "id": "colosseum",
                "title": "Colosseum",
                "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
                "short_text": "An oval amphitheatre in the centre of Rome, Italy, built of travertine limestone, tuff, and brick-faced concrete.",
                "year_built": "70-80 AD",
                "location": "Rome, Italy",
                "reference_url": "https://en.wikipedia.org/wiki/Colosseum"
            },
            {
                "id": "great-wall",
                "title": "Great Wall of China",
                "image": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=800",
                "short_text": "A series of fortifications made of stone, brick, tamped earth, wood, and other materials, generally built along an east-to-west line across the historical northern borders of China.",
                "year_built": "7th century BC - 17th century AD",
                "location": "China",
                "reference_url": "https://en.wikipedia.org/wiki/Great_Wall_of_China"
            },
            {
                "id": "machu-picchu",
                "title": "Machu Picchu",
                "image": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?w=800",
                "short_text": "A 15th-century Inca citadel located in the Eastern Cordillera of southern Peru on a 2,430-metre mountain ridge.",
                "year_built": "1450",
                "location": "Cusco Region, Peru",
                "reference_url": "https://en.wikipedia.org/wiki/Machu_Picchu"
            },
            {
                "id": "pyramids-giza",
                "title": "Pyramids of Giza",
                "image": "https://images.unsplash.com/photo-1539650116574-75c0c6d73c6e?w=800",
                "short_text": "Ancient Egyptian pyramid complex on the Giza Plateau, including the Great Pyramid of Giza, the Pyramid of Khafre, and the Pyramid of Menkaure.",
                "year_built": "2580-2510 BC",
                "location": "Giza, Egypt",
                "reference_url": "https://en.wikipedia.org/wiki/Giza_pyramid_complex"
            },
            {
                "id": "statue-liberty",
                "title": "Statue of Liberty",
                "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800",
                "short_text": "A neoclassical sculpture on Liberty Island in New York Harbor within New York City, a gift from the people of France.",
                "year_built": "1886",
                "location": "New York, USA",
                "reference_url": "https://en.wikipedia.org/wiki/Statue_of_Liberty"
            },
            {
                "id": "big-ben",
                "title": "Big Ben",
                "image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800",
                "short_text": "The nickname for the Great Bell of the striking clock at the north end of the Palace of Westminster in London.",
                "year_built": "1859",
                "location": "London, UK",
                "reference_url": "https://en.wikipedia.org/wiki/Big_Ben"
            },
            {
                "id": "christ-redeemer",
                "title": "Christ the Redeemer",
                "image": "https://images.unsplash.com/photo-1548013146-72479768bada?w=800",
                "short_text": "An Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil, created by French sculptor Paul Landowski.",
                "year_built": "1922-1931",
                "location": "Rio de Janeiro, Brazil",
                "reference_url": "https://en.wikipedia.org/wiki/Christ_the_Redeemer_(statue)"
            },
            {
                "id": "sydney-opera",
                "title": "Sydney Opera House",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
                "short_text": "A multi-venue performing arts centre in Sydney, Australia, designed by Danish architect Jørn Utzon.",
                "year_built": "1959-1973",
                "location": "Sydney, Australia",
                "reference_url": "https://en.wikipedia.org/wiki/Sydney_Opera_House"
            },
            {
                "id": "notre-dame",
                "title": "Notre-Dame Cathedral",
                "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
                "short_text": "A medieval Catholic cathedral in Paris, France, widely considered one of the finest examples of French Gothic architecture.",
                "year_built": "1163-1345",
                "location": "Paris, France",
                "reference_url": "https://en.wikipedia.org/wiki/Notre-Dame_de_Paris"
            },
            {
                "id": "sagrada-familia",
                "title": "Sagrada Familia",
                "image": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800",
                "short_text": "A large unfinished Roman Catholic minor basilica in Barcelona, Spain, designed by Catalan architect Antoni Gaudí.",
                "year_built": "1882-present",
                "location": "Barcelona, Spain",
                "reference_url": "https://en.wikipedia.org/wiki/Sagrada_Familia"
            }
        ]
    
    async def get_curated_monuments(self, limit: int = 12) -> List[Dict]:
        """
        Get curated monuments for the explore page
        """
        try:
            # Shuffle and return limited number of monuments
            shuffled = self.curated_monuments.copy()
            random.shuffle(shuffled)
            return shuffled[:limit]
            
        except Exception as e:
            print(f"Error getting curated monuments: {e}")
            return []
    
    async def get_monument_by_id(self, monument_id: str) -> Dict:
        """
        Get specific monument by ID
        """
        try:
            for monument in self.curated_monuments:
                if monument["id"] == monument_id:
                    return monument
            return {}
            
        except Exception as e:
            print(f"Error getting monument by ID: {e}")
            return {}
    
    async def search_monuments(self, query: str) -> List[Dict]:
        """
        Search monuments by name or location
        """
        try:
            query_lower = query.lower()
            results = []
            
            for monument in self.curated_monuments:
                if (query_lower in monument["title"].lower() or 
                    query_lower in monument["location"].lower() or
                    query_lower in monument["short_text"].lower()):
                    results.append(monument)
            
            return results
            
        except Exception as e:
            print(f"Error searching monuments: {e}")
            return []
