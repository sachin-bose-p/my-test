from fastapi import FastAPI

app = FastAPI()

# Configure logging
import logging
logging.basicConfig(level=logging.INFO)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Main entry point for running the FastAPI app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
