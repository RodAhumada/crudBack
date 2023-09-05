from fastapi import FastAPI
import uvicorn

from app.routers import user
from app.db.database import Base, engine

from fastapi.middleware.cors import CORSMiddleware

def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()
app.include_router(user.router)

if __name__=="__main__":
	uvicorn.run("main:app", port=8000,reload=True)

origins = [
      "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)