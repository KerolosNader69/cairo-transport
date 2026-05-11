"""Vercel serverless function handler for Cairo Transport API."""

import sys
import os

# Add the Cairo-Transport-main directory to the path
project_root = os.path.join(os.path.dirname(__file__), '..')
cairo_transport_dir = os.path.join(project_root, 'Cairo-Transport-main')
sys.path.insert(0, cairo_transport_dir)
sys.path.insert(0, project_root)

# Import and export the FastAPI app
from api import app

# Vercel will use this app instance
__all__ = ['app']
