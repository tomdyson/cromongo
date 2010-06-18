# Create your views here.

from django.conf import settings
from crm.shortcuts import render_with_context
from crm.utils import get_db

def home(request, template_name="crm/home.html"):
    return render_with_context( request, template_name, {} )
    
def person_details(request, person_id=person_id, template_name="crm/person_details.html")
    db = get_db()
    person = db.people.find_one({"_id": person_id})
    return render_with_context( request, template_name, {'person': person} )