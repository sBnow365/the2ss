# backend/src/agents/followup_agent.py

import google.generativeai as genai
from src.config.settings import GEMINI_API_KEY

class FollowupAgent:

    def __init__(self):

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def ask(self, tab: str, previous_context: str, question: str):

        prompt = f"""
You are an expert assistant.

The user previously received this {tab} analysis:

{previous_context}

Now the user asks:

{question}

Answer clearly based on the context.
If needed extend with additional knowledge.
"""

        response = self.model.generate_content(prompt)

        return response.text