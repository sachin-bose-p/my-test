import os

# Environment Variables

# Note: Use environment variables for secure connections
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Remove default credentials to avoid hardcoding
# DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# For frontend use, add the necessary variables as needed
# For frontend use, add the necessary variables as needed
FRONTEND_API_URL = os.getenv('FRONTEND_API_URL', 'http://localhost:3000/api')

# PostgreSQL Connection Settings
# Ensure these environment variables are set externally for security
DATABASE_HOST = os.getenv('DATABASE_HOST', '')
DATABASE_PORT = os.getenv('DATABASE_PORT', '')
DATABASE_NAME = os.getenv('DATABASE_NAME', '')
DATABASE_USER = os.getenv('DATABASE_USER', '')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Add any additional environment variable setups required for your application