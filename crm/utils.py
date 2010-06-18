import os, sys
import simplejson as json
from pymongo import Connection

def get_db():
    # Connect to and return a MongoDB database
    conn = Connection() # TODO: get connection details from settings
    db = conn.cromongo # would be a database per implementation in a SAAS future
    return db


def populate_default_fields(filename='fixtures/initial_fields.json'):
    """
    fields will be a Collection that contains details of attributes that other collections use

    Fields
     - collection 
     - label
     - name
     - type (text, int, float, list)
     - custom validation rule (1.1)


    var field = {
      'collection': 'People',
      'order': 1,
      'label': 'first name',
      'internal_name': 'first_name',
      'type': 'text'.
      'validation': ['is_name', 'is_not_null']
    }
    """

    f = open(filename, 'r')
    definitions = f.read()

    db = get_db()
    definitions_json = json.loads(definitions)
    out = db.fields.insert(definitions_json)
    
    f.close()



def get_fields(collection, as_dict=True):
    """
    Gets the field objects that reference the given Collection
    
    """
    
    db = get_db()
    
    fields = db.fields.find({'collection':collection})
    
    if as_dict:
        fields = dict(fields)
    
    return fields
    
    