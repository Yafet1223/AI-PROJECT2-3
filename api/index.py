"""
Vercel serverless function entry point for Django
This is a workaround to run Django on Vercel (not recommended)
"""
import os
import sys
from pathlib import Path

# Add project to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alternate_universe_backend.settings')

# Import Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def handler(request):
    """Vercel serverless function handler"""
    return application(request.environ, lambda status, headers: None)

