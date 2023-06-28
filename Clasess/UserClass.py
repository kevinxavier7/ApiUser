from Models.UserModel import User
from sqlalchemy import insert, update
from Utils.Tools import response, get_input_data, response_error
from Auth.SignIn import SignIn


class UserManager():
    def __init__(self, conn):
        self.db = conn
        self.signin = SignIn(conn)
    
    def create_user(self, event:dict):
        
        request = get_input_data(event) 
        
        request['password'] = self.signin.encode_password(request['password'])         
        
        self.db.add(
            insert(User).values(request)            
        )
        request.pop('password')
        
        return response(200, "user created sucessfull", request )
    
        
    def get_user(self, event:dict): 
        
        request = get_input_data(event)            
        
        if request:
            data = self.db.get(User, User.user_id == request['user_id'])
                               
        else:
            data = self.db.get_all(User)
        
        return response(200, "list users", data)
    
    
    def update_user(self, event:dict):
        
        request = get_input_data(event)
        
        user = self.db.get(User, User.user_id == request['user_id'])
        
        if user:        
            self.db.query( update(
                User).values(request).where(
                    User.user_id == request['user_id']
                ))                
            return response(200, "user updated sucessfull", request)
        
        return response_error(400, "User not found")