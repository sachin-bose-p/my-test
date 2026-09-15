import os

# Environment Variables

# Note: Use environment variables for secure connections
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# Remove default credentials to avoid hardcoding
# DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# For frontend use, add the necessary variables as needed
# For frontend use, add the necessary variables as needed
FRONTEND_API_URL = os.getenv('FRONTEND_API_URL', 'http://localhost:3000/api')

# PostgreSQL Connection Settings
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
# Update the connection settings as required
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'mydatabase')
DATABASE_USER = os.getenv('DATABASE_USER', 'username')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Add any additional environment variable setups required for your application