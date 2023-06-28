from Clasess.AuthClass import AuthClss
from Database.Database import Database
from Database.Connection import db_url




def login(event, context):
    conn = Database(db_url)
    auth = AuthClss(conn)
    return auth.authentication(event)
    
    
    
    
    