# Create your views here.

from django.conf import settings
from crm.shortcuts import render_with_context
from crm.utils import get_db
from pymongo.objectid import ObjectId

def home(request, template_name="crm/home.html"):
    return render_with_context( request, template_name, {} )

    
def person_details(request, person_id, template_name="crm/person_details.html"):
    db = get_db()
    oid = ObjectId(person_id) # TODO: catch InvalidId
    person = db.people.find_one({"_id": oid})
    person_dict = dict(person.items())
    return render_with_context( request, template_name, 
        {'person': person_dict} )