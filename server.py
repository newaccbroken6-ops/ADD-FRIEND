#!/usr/bin/env python3
"""
Vercel-compatible Server for FreeFire API
This script serves the API endpoints in a serverless environment.
"""

import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the main app
try:
    from app import app
except ImportError as e:
    print(f"Error importing app: {e}")
    sys.exit(1)

# The app is already configured in app.py, so we just need to export it
# Vercel will automatically use this as the serverless function
application = app

# For local testing
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[🚀] Starting FreeFire API Manager on port {port} ...")
    application.run(host='0.0.0.0', port=port, debug=False)
