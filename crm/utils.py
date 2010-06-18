from pymongo import Connection

def get_db():
    # Connect to and return a MongoDB database
    conn = Connection() # TODO: get connection details from settings
    db = conn.cromongo # would be a database per implementation in a SAAS future
    return db