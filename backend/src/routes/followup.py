from fastapi import APIRouter
from pydantic import BaseModel
from src.orchestrator.travel_orchestrator import TravelOrchestrator

router = APIRouter()
orchestrator = TravelOrchestrator()

class FollowupRequest(BaseModel):
    tab: str
    question: str


@router.post("/followup")
async def followup(req: FollowupRequest):

    answer = await orchestrator.followup(
        tab=req.tab,
        question=req.question
    )

    return {"answer": answer}