from sqlalchemy import  Integer, String, Column, DateTime, Numeric
from .BaseModel import Base
from sqlalchemy.sql.functions import current_timestamp
from Database.Database import Database
from Database.Connection import db_url
import json




class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    full_name = Column(String(200))
    email = Column(String(100))
    created_at = Column(String(20), default = current_timestamp())
    updated_at = Column(String(20), onupdate = current_timestamp())




def create_table_user(event, context):
    db = Database(db_url)

    Base.metadata.create_all(db.engine)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Table created successfully'
        })
    }