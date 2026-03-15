# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from src.api.routes import router

# app = FastAPI(title="Travel Vision API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(router)
from fastapi import FastAPI
from src.routes import analyze
from src.routes.followup import router as followup_router
from src.routes.news import router as news_router 
from src.routes.images import router as images_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(analyze.router)
app.include_router(followup_router, prefix="/api")
app.include_router(news_router)
app.include_router(images_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)