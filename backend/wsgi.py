import os
from django.core.wsgi import get_wsgi_application

# Make sure this matches your project folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
