import asyncio
from src.agents.vision_agent import VisionAgent
from src.agents.geo_agent import GeoAgent
from src.agents.cultural_agent import CulturalAgent
from src.agents.travel_agent import TravelAgent
import tempfile
# from src.agents.travel_agent import TravelAgent

class TravelOrchestrator:

    def __init__(self):
        self.vision_agent = VisionAgent()
        self.geo_agent = GeoAgent()
        self.cultural_agent = CulturalAgent()
        self.travel_agent = TravelAgent()

    async def process_image(self, image_bytes,user_location=None):

        # Step 1: Detect place
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(image_bytes)
            temp_path = tmp.name
        place_context = await self.vision_agent.analyze(temp_path)

        # Step 2: Run domain agents in parallel
        geo_task = self.geo_agent.analyze(place_context)
        cultural_task = self.cultural_agent.analyze(place_context)
        travel_task = self.travel_agent.analyze(place_context,user_location)

        geo, culture,travel= await asyncio.gather(
            geo_task,
            cultural_task,
            travel_task
        )

        return {
            "place": place_context,
            "geo": geo,
            "culture": culture,
            "travel":travel
        }