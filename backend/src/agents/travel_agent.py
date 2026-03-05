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
        prompt= f"""
You are a cultural analysis agent.

The place has already been identified and MUST NOT be re-identified or questioned.

PLACE DETAILS:
- Name: {place_context.get("name")}
- City: {place_context.get("city")}
- Country: {place_context.get("country")}
- Type: {place_context.get("place_type")}
-Latitude:{user_location.get("lat")}
-Longitude:{user_location.get("lon")}


STRICT OUTPUT RULES:
- Return ONLY valid JSON
- Do NOT use markdown
- Do NOT include explanations
- Do NOT wrap output in ``` or ```json

Required JSON schema:
{{
  "distance_km": "",

  "transport_options": [
    {
      "budget_level": "",
      "approx_cost_usd": "",
      "method": "",
      "timeline": "",
      "steps": [""]
    }
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

        # Handle accidental markdown wrapping just in case
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if match:
            cleaned_text = match.group(1)
        else:
            cleaned_text = text.strip()

        try:
            parsed = json.loads(cleaned_text)
        except json.JSONDecodeError as e:
            print("----- DEBUG: FAILED TO PARSE CULTURAL JSON -----")
            print(cleaned_text)
            print("----------------------------------------------")
            raise ValueError(f"JSON parsing failed at position {e.pos}")

        # Basic schema validation
        required_keys = [
            "distance",
            "suggested_transport",
            "tips"
        ]
        for key in required_keys:
            if key not in parsed:
                raise ValueError(f"Missing key in Travel Agent output: {key}")

        return parsed