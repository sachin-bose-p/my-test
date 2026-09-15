from fastapi import FastAPI, Depends, Request

# Create FastAPI application instance
app = FastAPI()

# Swagger endpoint for documentation
# The OpenAPI documentation is served automatically by FastAPI at `/docs`
# Redoc is also available at `/redoc`
import logging

import os
from dotenv import load_dotenv
load_dotenv() # Loading environment variables from .env file

# Configure root logging
logging.root.setLevel(logging.INFO)

# Configure custom logging format and output
log_format = '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)

# Application logger
application_logger = logging.getLogger('application')
application_logger.propagate = False

# Error logger
error_logger = logging.getLogger('error')

# Error handler for writing logs to a file
error_handler = logging.FileHandler('error.log', mode='a')  # Append mode
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter(log_format))

# Ensure error logs do not propagate to global logger
error_logger.addHandler(error_handler)
error_logger.propagate = False



from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

# Pydantic model for response consistency
class ResponseModel(BaseModel):
    data: dict
    message: str = "Operation successful"
from fastapi.exception_handlers import http_exception_handler

# Function to handle global exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    msg = f"Unexpected error: {exc}"
    error_logger.error(msg)
    return JSONResponse(status_code=500, content={"message": msg})

# Response wrapper function

# Modify the response wrapper function implementation if necessary for fixes

def response_wrapper(data: dict, message: str = "Operation successful", status_code: int = 200):
    # Properly handle data serialization and ensure compatibility without defaults
    if not isinstance(data, dict):
        raise ValueError("Provided data must be a dictionary type.")
    return JSONResponse(content={"data": data, "message": message}, status_code=status_code)

# Function to handle request validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_logger.error(f"Validation error: {exc}")
    return response_wrapper({}, f"Validation error: {exc}", status_code=422)

import logging
from fastapi import Depends, Request

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
job_logger = logging.getLogger('job')
job_logger.setLevel(logging.INFO)

# Create a logger for error logs
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)

# Configure error logging to log messages to a file
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
error_logger.addHandler(file_handler)

# Middleware to log requests and responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    audit_logger.info(f"Request {request.method} {request.url.path}")
    response = await call_next(request)
    audit_logger.info(f"Response status: {response.status_code}")
    return response


# Route for triggering audit logging
@app.post('/audit-log')
async def log_audit_event(request: Request, db: Session = Depends(get_db)):
    """Endpoint to log audit events into the database"""
    try:
        event_data = await request.json()
        event = Audit(action=event_data.get('action'))
        db.add(event)
        db.commit()
        audit_logger.info(f"Audit event logged: {event.action}")
        return response_wrapper({'message': 'Audit event logged successfully'})
    except Exception as e:
        error_logger.error(f"Failed to log audit event: {e}")
        return response_wrapper({'message': 'Failed to log audit event.', 'error': str(e)}, status_code=500)

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
from database import get_engine, Base, get_db


job_logger = logging.getLogger('job')
job_logger.setLevel(logging.INFO)

import logging
logging.basicConfig(level=logging.INFO)

# Health check endpoint
@app.get('/test-db-connection')
def test_db_connection(db: Session = Depends(get_db)):
    """Test database connection injection"""
    try:
        # Perform a simple session query or action to ensure the session is working
        # This is just a placeholder action
        db.query(User).first()
        return response_wrapper({'message': 'Dependency Injection for DB successful!'})
    except Exception as e:
        error_logger.error(f'Dependency Injection test failed: {e}')
        return response_wrapper({'message': 'Dependency Injection test failed.', 'error': str(e)}), 500

@app.get('/health')
def health_check():
    """Health check endpoint returns application status"""
    return response_wrapper({'status': 'healthy'}, "Health check successful")

# Ensure that the `/items/{item_id}` endpoint uses ResponseModel correctly
# Updating handler to ensure compliance with FastAPI's response models
@app.get('/items/{item_id}', response_model=dict)
def get_item(item_id: int, db: Session = Depends(get_db)):
    try:
        db.query(User).filter(User.id == item_id).first()
        return response_wrapper({'message': 'Item retrieved successfully!'}, "Item Retrieval Successful")
    except Exception as e:
        error_logger.error(f'Error retrieving item: {e}')
        return response_wrapper({'message': 'Error retrieving item.', 'error': str(e)}, "Item Retrieval Failed.")

@app.get('/db-verify')
def verify_db_connection():
    """Verify database connectivity through a basic engine connect/close"""
    try:
        engine = get_engine()
        connection = engine.connect()
        connection.close()
        return response_wrapper({'message': 'Database connectivity successful!'}, "DB verified")
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return response_wrapper({'message': 'Database connectivity failed.', 'error': str(e)}, "DB verification failed."), 500
@app.get('/health')
def health_check():
    return {'status': 'healthy'}

@app.get('/db-verify')
def verify_db_connection():
    try:
        engine = get_engine()
        connection = engine.connect()
        connection.close()
        return {'message': 'Database connectivity successful!'}
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500
def health_check():
    return {'status': 'healthy'}

@app.get('/db-verify')
def verify_db_connection():
    try:
        engine = get_engine()
        connection = engine.connect()
        connection.close()
        return {'message': 'Database connectivity successful!'}
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500
@app.get('/health')
def health_check():
    return {'status': 'healthy'}

# Create logger for application logs
application_logger = logging.getLogger('application')
application_logger.setLevel(logging.INFO)

# Create logger for audit logs
audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)

# Create logger for security logs
security_logger = logging.getLogger('security')
security_logger.setLevel(logging.INFO)

# Create logger for error logs
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)

# Create logger for job logs
job_logger = logging.getLogger('job')
job_logger.setLevel(logging.INFO)

# File handler for logging errors to file
error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)
# Middleware to handle cross-cutting concerns
import time

@app.middleware("http")
async def log_and_enhance_requests(request: Request, call_next):
    # Example middleware: timing request processing
    start_time = time.time()
    application_logger.info(f"Received request: {request.method} {request.url}")
    
    # Continue processing the request
    response = await call_next(request)
    
    # Enhance logging with request processing time
    process_time = time.time() - start_time
    application_logger.info(f"Processed request in {process_time:.2f} sec - Status: {response.status_code}")
    
    return response
@app.middleware("http")
async def log_and_enhance_requests(request: Request, call_next):
    # Example middleware: timing request processing
    start_time = time.time()
    application_logger.info(f"Received request: {request.method} {request.url}")
    
    # Continue processing the request
    response = await call_next(request)
    
    # Enhance logging with request processing time
    process_time = time.time() - start_time
    application_logger.info(f"Processed request in {process_time:.2f} sec - Status: {response.status_code}")
    
    return response

# Verify Database Connectivity
@app.get('/db-verify')
def verify_db_connection():
    try:
        engine = get_engine()
        connection = engine.connect()
        connection.close()
        return {'message': 'Database connectivity successful!'}
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500

# Dependency Injection Setup

from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

# Example endpoint utilizing dependency injection
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id, "db_status": "connected"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Configure logging
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Dependency Injection Setup

from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id}

# Dependency Injection Setup

from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id}

# Additional API endpoints can be added below

# GET endpoint for profile
@app.get('/profile')
async def get_profile(db: Session = Depends(get_db)):  
    profiles = db.query(UserProfiles).all()
    return profiles  

# PUT endpoint for updating profile
@app.put('/profile')
async def update_profile(profile: UserProfiles, db: Session = Depends(get_db)):
    db.query(UserProfiles).filter(UserProfiles.id == profile.id).update(profile.dict())
    db.commit()
    return profile

# POST endpoint for uploading image
@app.post('/profile/upload-image')
async def upload_image(file: UploadFile, db: Session = Depends(get_db)):
    # Here you would handle saving the image to a directory and update profile with the image URL.
    return {'filename': file.filename}

# Endpoint to verify database connectivity
@app.get('/db-verify')
def verify_db_connection():
    try:
        engine = get_engine()
        conn = engine.connect()
        conn.close()
        return {'message': 'Database connectivity successful!'}
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500

# Add another endpoint to verify database connectivity for health checks.
@app.get('/db-verify')
def verify_db_connection():
    try:
        engine = get_engine()
        conn = engine.connect()
        conn.close()
        return {'message': 'Database connectivity successful!'}
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500
    except Exception as e:
        error_logger.error(f'Database connectivity error: {e}')
        return {'message': 'Database connectivity failed.', 'error': str(e)}, 500

# Global middleware example
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import get_db

# Role verification middleware
@app.middleware("http")
async def role_verification(request: Request, call_next):
    # Obtain the user's role from the request (assumes you have a way to extract user roles)
    user_role = request.headers.get('X-User-Role')

    # Placeholder for role checking logic
    if user_role not in ['System Admin', 'Premium User', 'Basic User', 'Analyst']:
        raise HTTPException(status_code=403, detail="Unauthorized access")

    response = await call_next(request)
    return response
@app.middleware("http")
async def custom_global_middleware(request: Request, call_next):
    # Log the request - this is the global middleware handling
    audit_logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    audit_logger.info(f"Response status: {response.status_code}")
    return response
    # Log the request - you can customize this further
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    # Log the response
    logging.info(f"Response status: {response.status_code}")
    return response

@app.get('/db-test')
def db_test(db: Session = Depends(get_db)):
    return {'message': 'Database connection working!'}

@app.get('/db-test')
def db_test(db: Session = Depends(get_db)):
    return {'message': 'Database connection working!'}

# Job Log Example Endpoint
@app.post('/job/log')
async def log_job_event(event: dict):
    job_logger.info(f'Job event: {event}')
    return {'success': True, 'message': 'Job log recorded'}


# Audit Log Example Endpoint
@app.post('/audit/log')
async def log_audit_event(event: dict):
    audit_logger.info(f'Audit event: {event}')
    return {'success': True, 'message': 'Audit log recorded'}

# Example use of response wrapper in an endpoint
@app.get('/items/{item_id}', response_model=None)
def get_item(item_id: int):
    """Example endpoint that uses the response wrapper"""
    data = {"item_id": item_id, "name": "Example Item"}
    return response_wrapper(data, "Item fetched successfully")

def response_wrapper(data: any, message: str = None):
    return ResponseModel(data, message)
# Example use of response wrapper in an endpoint
@app.get('/items/{item_id}')

def response_wrapper(data: any, message: str = None):
    return ResponseModel(data, message)
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
    return response_wrapper(data=item)

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


# Dependency Injection Setup
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

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

# FastAPI automatic OpenAPI schema generation is included by default, no additional setup is required.
# Ensure that the FastAPI instance is correctly configured to expose the API documentation.


@app.get("/api")

def security_log_event(event: dict):
    security_logger.info(f'Security event: {event}')
    return {'success': True, 'message': 'Security log recorded'}
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
