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
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(analyze.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)