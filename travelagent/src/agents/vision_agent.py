import google.generativeai as genai
from src.config.settings import GEMINI_API_KEY
import json
import re

class VisionAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def analyze(self, image_path: str) -> dict:
        image_file = genai.upload_file(image_path)

        prompt = """
You are a vision analysis agent.

STRICT OUTPUT RULES:
- Return ONLY valid JSON.
- Do NOT wrap the response in markdown.
- Do NOT include ``` or ```json.
- Do NOT include explanations
- Do NOT use markdown

Required JSON schema:
{
  "landmark": "",
  "location_hint": "",
  "scene_type": [],
  "confidence": 0.0,
  "visual_tags": []
}

"""

        response = self.model.generate_content([prompt, image_file])
       # print(response.text)
        raw = response.text
        print("----- RAW MODEL OUTPUT START -----")
        print(raw)
        print("----- RAW MODEL OUTPUT END -----")
        return self._parse_response(response.text)

def _parse_response(self, text: str) -> dict:
    """
    Robustly extract JSON from LLM output.
    Handles markdown fences, extra text, and whitespace.
    """
    try:
        # Remove markdown code fences if present
        text = re.sub(r"```(?:json)?", "", text)
        text = text.replace("```", "").strip()

        # Extract JSON object
        json_str = re.search(r"\{.*\}", text, re.DOTALL).group()

        return json.loads(json_str)

    except Exception as e:
        raise ValueError(f"Invalid JSON returned:\n{text}") from e