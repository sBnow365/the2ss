import google.generativeai as genai
from src.config.settings import GEMINI_API_KEY
import json
import re


class GeoAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def analyze(self, place_context: dict) -> dict:
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
You are a geography analysis agent.

The place has already been identified and MUST NOT be re-identified or questioned.

PLACE DETAILS:
- Name: {place_context.get("name")}
- City: {place_context.get("city")}
- Country: {place_context.get("country")}
- Type: {place_context.get("place_type")}

STRICT OUTPUT RULES:
- Return ONLY valid JSON
- Do NOT use markdown
- Do NOT include explanations
- Do NOT wrap output in ``` or ```json

Required JSON schema:
{{
  "landforms": [
    "short bullet points"
  ],
  "weather_info": [
    {{
      "season": "",
      "summary": ""
    }}
  ],
  "rain_natural_resources": [
    "short bullet points"
  ],
  "flora_fauna": [
    "short bullet points"
  ]
  "population_facts": [
    "short bullet points"
  ]
}}
"""

        response = self.model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )

        raw = response.text
        print("----- RAW geographical MODEL OUTPUT START -----")
        print(raw)
        print("----- RAW geographical MODEL OUTPUT END -----")

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
            print("----- DEBUG: FAILED TO PARSE geographical JSON -----")
            print(cleaned_text)
            print("----------------------------------------------")
            raise ValueError(f"JSON parsing failed at position {e.pos}")

        # Basic schema validation
        required_keys = [
            "landforms",
            "weather_info",
            "rain_natural_resources",
            "flora_fauna",
            "population_facts"
        ]
        for key in required_keys:
            if key not in parsed:
                raise ValueError(f"Missing key in Geographical output: {key}")

        return parsed
