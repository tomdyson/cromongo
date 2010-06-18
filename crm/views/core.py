# Create your views here.

from django.conf import settings
from crm.shortcuts import render_with_context

def home(request, template_name="crm/home.html"):
    
    return render_with_context( request, template_name, {} )