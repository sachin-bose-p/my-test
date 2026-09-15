import os

# Environment Variables

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')

# For frontend use, add the necessary variables as needed
FRONTEND_API_URL = os.getenv('FRONTEND_API_URL', 'http://localhost:3000/api')

# Add any additional environment variable setups required for your application