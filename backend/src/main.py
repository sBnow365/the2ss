from src.agents.cultural_agent import CulturalAgent
from src.agents.vision_agent import VisionAgent
from src.agents.geo_agent import GeoAgent
def predict_location_from_image(image_path):
    """
    LLM/Vision model stub.
    Replace later with real model call.
    """
    return {
        "place":"Parthenon",
        "city": "Athens",
        "country": "Greece",
        "confidence": 0.87
    }


def get_user_location(city, country):
    return {
        "city": city.strip().title(),
        "country": country.strip().title()
    }


def build_travel_context(user_location, destination):
    return {
        "source": user_location,
        "destination": destination
    }


if __name__ == "__main__":
    # user_location = get_user_location("pune", "india")
    # destination = predict_location_from_image("temple.jpg")

    # context = build_travel_context(user_location, destination)

    # print(context)
    # vision_output = {
    # "place_type": "monument",
    # "name": "Parthenon",
    # "city": "Athens",
    # "country": "Greece",
    # "confidence": 0.98
    # }



    # print(culture)
    # vision_agent = VisionAgent()
    # place_context = vision_agent.analyze("data/images/i2.jpg")
    # cultural_agent = CulturalAgent()
    # culture = cultural_agent.analyze(place_context)
    place_context={
            "place_type": "historic site",
            "name": "Parthenon",
            "city": "Athens",
            "country": "Greece",
            "confidence": 1.0
        }
    geo_agent=GeoAgent()
    geogr=geo_agent.analyze(place_context)
    print(geogr)
