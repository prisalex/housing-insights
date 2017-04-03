import sys
sys.path.insert(0, './vendor')

import datetime
import decimal
import json

from sqlalchemy import create_engine, inspect, types
from sqlalchemy.engine import reflection


class HiJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
            return o.isoformat()    
        elif isinstance(o, decimal.Decimal):
            return float(o)

        return json.JSONEncoder.default(self, o)

'''
Returns raw DB table in CSV format. 
'''
def rawtable(event, context):
    if event['queryStringParameters'] is None:
        return create_error_body("Query param tablename is required")
    elif 'tablename' not in event['queryStringParameters']:
        return create_error_body("Query param tablename is required")

    table_name = event['queryStringParameters']['tablename']

    data = get_table(table_name)
    if data is None:
        return create_error_body("requested table does not exist")

    return {
        "headers": {
            "Access-Control-Allow-Origin" : "*"# Required for CORS support to work          
        },
        "statusCode": 200,        
        "body": json.dumps(data, cls=HiJsonEncoder)
    }

def create_error_body(errorMessage):
    return {
        "statusCode": 400,
        "body": json.dumps({ "message": errorMessage })
    }       



def get_table(tablename):
    db_conn = get_database_connection()    

    inspector = get_database_inspector()

    table_names = inspector.get_table_names()
    if tablename not in table_names:
        return None

    results = db_conn.execute("SELECT * from "+ tablename + " limit 100;")
        
    columns = inspector.get_columns(tablename)    
    
    rowObjs = []
    for row in results:
        rowObj = {}
        for column in columns:
            rowObj[column['name']]=row[column['name']]
        rowObjs.append(rowObj)   
        
    return rowObjs


def get_database_inspector():
    engine = get_database_engine()
    return inspect(engine)

def get_connect_str():
    #fill this in with the real connection string to run
    return ""    

def get_database_connection():
    # Connect to the database    
    engine = create_engine(get_connect_str())
    database_connection = engine.connect()
    return database_connection

def get_database_engine():
    # Connect to the database
    connection_string = get_connect_str()
    engine = create_engine(connection_string)
    return engine