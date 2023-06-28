import jwt
import datetime


class Auth():
    def __init__(self, secret_key, expiration_hour) :
        self.secret_key = secret_key
        self.expiration_hour = expiration_hour
        
    def generate_token(self, user_id):
                
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() +  datetime.timedelta(hours=self.expiration_hour)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')        
        
        return token
        
     
    def verify_token(self, token): 
        try:
            payload = jwt.decode(token, self.secret_key, algorithms='HS256')  
            return True,payload['user_id']
        except jwt.ExpiredSignatureError:
            return False,"expired token"
        except jwt.InvalidTokenError:
            return False,"invalid token"
        
              
    
