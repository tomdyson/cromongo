from pymongo import Connection

def get_db():
    # Connect to and return a MongoDB database
    conn = Connection() # TODO: get connection details from settings
    db = conn.cromongo # would be a database per implementation in a SAAS future
    return db



def get_fields(Collection):
    """
    Gets the field objects that reference the given Collection
    
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
    
    db = get_db()
