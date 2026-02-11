"""
Vercel Entry Point for FreeFire API
"""
from app import app

# Vercel expects the Flask app to be exported as 'app' or 'handler'
application = app

if __name__ == "__main__":
    application.run()