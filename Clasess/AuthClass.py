from Auth.Auth import Auth
from Auth.SignIn import SignIn
from os import environ
from Utils.Tools import response, response_error

class AuthClss():
    def __init__(self, conn):
        self.db = conn
        self.auth = Auth(environ.get('SECRET_KEY'), 1)
        self.sign = SignIn(conn)
    
    def authentication(self, event:dict):
        
        user_id = self.sign.verify_user(event)
        
        if user_id:                    
            token = self.auth.generate_token(user_id)                        
            return response(200, "login successful",
                            {   
                             'user_id': user_id,
                             'token': token,                               
                            })
        return response_error(400, "invalid username or password")