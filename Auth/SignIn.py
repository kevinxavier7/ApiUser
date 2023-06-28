from Models.UserModel import User
from sqlalchemy import select
import bcrypt
from Utils.Tools import get_input_data


class SignIn():
    def __init__(self, conn):
        self.db = conn
        
    def encode_password(self, password):
        
        bytes = str(password).encode('utf-8')
        encode_password = bcrypt.hashpw( bytes, bcrypt.gensalt()) 
        return encode_password    
            
    
    def verify_user(self, data:dict):   
        
        request = get_input_data(data)         
        
        user = self.db.query(select(User.user_id, User.password).where(
                User.username == request['username']
            ))        
        
        if user: 
            password = str(request['password']).encode('utf-8')                   
            if bcrypt.checkpw(password, str(user[0]['password']).encode('utf-8')):
                return user[0]['user_id']
        return False
            
        
    