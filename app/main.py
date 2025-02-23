from fastapi import FastAPI
from app.handlers.student_handler import router as student_router
import os

app = FastAPI()
app.include_router(student_router)

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run(app, host=host, port=port)
