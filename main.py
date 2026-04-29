from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import test_controller
from controllers import auth_controller
from controllers import user_controller
from controllers import admin_controller
from database.db import engine, Base
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

Base.metadata.create_all(bind=engine)
app.include_router(test_controller.router)
app.include_router(auth_controller.router)
app.include_router(user_controller.router)
app.include_router(admin_controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)