from fastapi import FastAPI

app = FastAPI()

# Configure logging
import logging
from fastapi import Depends, Request

# Import FastAPI for the React application
import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Setting the logging format
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger for application logs
audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)

# Create a logger for security logs
security_logger = logging.getLogger('security')
security_logger.setLevel(logging.INFO)

# Create a logger for error logs
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)

# Create a logger for job logs
from sqlalchemy.orm import Session
from database import get_engine, Base


job_logger = logging.getLogger('job')
job_logger.setLevel(logging.INFO)

import logging
logging.basicConfig(level=logging.INFO)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Additional API endpoints can be added below

# Response Wrapper

# Cleaned up duplicate ResponseModel class definitions


class ResponseModel:
    def __init__(self, data: any, message: str = None):
        self.data = data
        self.message = message
        self.success = True

    def to_dict(self):
        return {
            'success': self.success,
            'message': self.message,
            'data': self.data
        }

# Example use of response wrapper in an endpoint
@app.get('/items/{item_id}', response_model=ResponseModel)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()  # Assuming 'Item' is a model class.
    if item is None:
        return ResponseModel(data=None, message='Item not found')
    return ResponseModel(data=item)

class ResponseModel:
    def __init__(self, data: any, message: str = None):
        self.data = data
        self.message = message
        self.success = True

    def to_dict(self):
        return {
            'success': self.success,
            'message': self.message,
            'data': self.data
        }

# Example use of response wrapper in an endpoint
@app.get('/items/{item_id}', response_model=ResponseModel)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()  # Assuming 'Item' is a model class.
    if item is None:
        return ResponseModel(data=None, message='Item not found')
    return ResponseModel(data=item)

# Global Exception Handler
@app.exception_handler(Exception) 
async def global_exception_handler(request: Request, exc: Exception):
    error_logger.error(f'Unexpected error: {exc}')  # Log the error details
    return JSONResponse(
        status_code=500,
        content={'message': 'An unexpected error occurred. Please try again later.'}
    )
    error_logger.error(f'Unexpected error: {exc}')  # Log the error details
    return JSONResponse(
        status_code=500,
        content={'message': 'An unexpected error occurred. Please try again later.'}
    )

from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_engine, Base

# Dependency to get DB session
def get_db():
    db = get_engine()  # Create database engine
    try:
        yield db
    finally:
        db.dispose()
from sqlalchemy.orm import Session
from database import get_engine, Base

# Dependency to get DB session

def get_db():
    db = get_engine()  # Create database engine
    try:
        yield db
    finally:
        db.dispose()

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id}


# Swagger and OpenAPI configurations

# Middleware to log requests and responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    audit_logger.info(f"Request {request.method} {request.url.path}")
    response = await call_next(request)
    audit_logger.info(f"Response status: {response.status_code}")
    return response

@app.get('/docs', include_in_schema=False)  
async def swagger_ui():  
    return RedirectResponse(url='/docs')


@app.get("/api")
def api_endpoint():
    return {"message": "API is operational"}
    return {"message": "API is operational"}


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
