from fastapi import APIRouter
from pydantic import BaseModel

from src.orchestrator.followup_orchestrator import FollowupOrchestrator

router = APIRouter()

orchestrator = FollowupOrchestrator()


class FollowupRequest(BaseModel):
    session_id: str
    tab: str
    question: str


@router.post("/followup")
def followup(req: FollowupRequest):

    print("\n========== FOLLOW UP REQUEST ==========")
    print("Session ID :", req.session_id)
    print("Tab        :", req.tab)
    print("Question   :", req.question)
    print("=======================================\n")

    result = orchestrator.handle_followup(
        session_id=req.session_id,
        tab=req.tab,
        question=req.question
    )

    print("\n========== GEMINI FOLLOW UP ANSWER ==========")
    print(result)
    print("=============================================\n")

    return result