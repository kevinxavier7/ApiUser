from Database.Database import Database
from Database.Connection import db_url
from Auth.Auth import Auth
from os import environ
from Utils.Tools import response_error

def authorized(func):   
    
    def wrapper(event, context):         
        
        try:
            auth = Auth(environ.get('SECRET_KEY'), 1)
            token = str(event['headers']['authorization']).replace('Bearer ','')
            
            verify_token = auth.verify_token(token)
            
            if verify_token[0]:
                conn = Database(db_url)
                result = func(event, context, conn)
                return result
            return response_error(400, verify_token[1])
        except Exception as e:
            return str(e)
    return wrapper