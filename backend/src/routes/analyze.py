from fastapi import APIRouter, UploadFile,Form
from src.orchestrator.travel_orchestrator import TravelOrchestrator

router = APIRouter()
orchestrator = TravelOrchestrator()

@router.post("/analyze")
async def analyze_image(
    file: UploadFile,
    lat:float|None=Form(None),
    lon:float|None=Form(None)
    ):

    image = await file.read()

    result = await orchestrator.process_image(image,
                                              user_location={"lat":lat,"lon":lon}
                                              )
    print(result)

    return result