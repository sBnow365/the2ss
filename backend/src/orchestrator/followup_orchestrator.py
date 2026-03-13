# backend/src/orchestrator/followup_orchestrator.py

from src.utils.context_store import context_store
from src.agents.followup_agent import FollowupAgent


class FollowupOrchestrator:

    def __init__(self):

        self.agent = FollowupAgent()

    def handle_followup(self, session_id: str, tab: str, question: str):

        context = context_store.get(session_id, tab)

        if not context:
            return {
                "error": f"No context found for {tab}. Run analysis first."
            }

        answer = self.agent.ask(
            tab=tab,
            previous_context=context,
            question=question
        )

        return {
            "tab": tab,
            "question": question,
            "answer": answer
        }