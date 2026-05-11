"""Vercel serverless function handler for Cairo Transport API."""

import sys
import os

# Add the Cairo-Transport-main directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Cairo-Transport-main'))

# Import the FastAPI app
from api import app

# Vercel expects a handler function
handler = app
