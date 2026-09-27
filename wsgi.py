"""
WSGI config for GlaucoFusion-XAI project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glaucofusion.settings')

application = get_wsgi_application()
