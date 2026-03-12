import google.generativeai as genai
from src.config.settings import GEMINI_API_KEY
from src.utils.async_utils import run_blocking
import json
import re

class TravelAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    async def analyze(self, place_context: dict,user_location) -> dict:
        """
        place_context example:
        {
            "place_type": "historic site",
            "name": "Parthenon",
            "city": "Athens",
            "country": "Greece",
            "confidence": 1.0
        }
        """
        prompt = f"""
    You are a travel planning agent.

    The destination has already been identified and MUST NOT be re-identified.

    DESTINATION DETAILS:
    - Name: {place_context.get("name")}
    - City: {place_context.get("city")}
    - Country: {place_context.get("country")}
    - Type: {place_context.get("place_type")}

    USER LOCATION:
    - Latitude: {user_location.get("lat")}
    - Longitude: {user_location.get("lon")}

    STRICT OUTPUT RULES
    - Return ONLY valid JSON
    - Do NOT include explanations
    - Do NOT include markdown
    - Do NOT wrap output in ``` or ```json
    - ALL keys must appear even if estimates are required

    Budget levels must be one of: Low, Medium, High.

    Steps should be short travel actions such as:
    "Take metro to airport"
    "Fly Delhi → Athens"
    "Taxi to destination"

    Required JSON schema:

    {{
    "distance_km": "distance between user location and destination in kilometres",

    "transport_options": [
        {{
        "budget_level": "",
        "approx_cost_usd": "",
        "method": "",
        "timeline": "",
        "steps": [""]
        }}
    ],

    "tips": ["short bullet points"]
    }}

    Provide 2–3 transport options if possible.
    """
        response = await run_blocking(
            self.model.generate_content,
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        raw = response.text
        # print("----- RAW CULTURAL MODEL OUTPUT START -----")
        # print(raw)
        # print("----- RAW CULTURAL MODEL OUTPUT END -----")

        return self._parse_response(raw)
    
    def _parse_response(self, text: str) -> dict:
        if not text:
            raise ValueError("The model returned an empty response.")

        match = re.search(r"```(?:json)?\s*(\{[\s\S]*\})\s*```", text)

        if match:
            cleaned_text = match.group(1)
        else:
            cleaned_text = text.strip()

        try:
            parsed = json.loads(cleaned_text)
        except json.JSONDecodeError as e:
            print("----- DEBUG: FAILED TO PARSE TRAVEL JSON -----")
            print(cleaned_text)
            print("----------------------------------------------")
            raise ValueError(f"JSON parsing failed at position {e.pos}")

        required_keys = [
            "distance_km",
            "transport_options",
            "tips"
        ]

        for key in required_keys:
            if key not in parsed:
                raise ValueError(f"Missing key in TravelAgent output: {key}")

        for option in parsed.get("transport_options", []):
            required_transport_keys = [
                "budget_level",
                "approx_cost_usd",
                "method",
                "timeline",
                "steps"
            ]

            for key in required_transport_keys:
                if key not in option:
                    raise ValueError(f"Missing key in transport option: {key}")

            if isinstance(option.get("steps"), str):
                option["steps"] = [option["steps"]]

        return parsed