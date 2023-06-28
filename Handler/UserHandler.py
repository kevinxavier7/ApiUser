from Utils.authorized import authorized
from Clasess.UserClass import UserManager


@authorized
def api_user(event, context, conn):
    
    user = UserManager(conn)
    
    methods = {
        'POST': user.create_user,
        'GET' : user.get_user,
        'PUT' : user.update_user,
    }
    
    data = methods.get(event['requestContext']['http']['method'])
   
    return data(event)