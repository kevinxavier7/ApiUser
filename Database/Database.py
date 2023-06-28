from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self, db_url=None):        
        self.engine= create_engine(db_url) 
        self.Session = sessionmaker(bind=self.engine)
    
    def create_session(self):
        self.session = self.Session()
        return self.session   
        
    def get(self, table, condicion):
        session = self.create_session()
        result = session.query(table).filter(condicion)                 
        session.close()                       
        return [row.as_dict() for row in result] 
    
    def get_all(self, table):
        session = self.create_session()
        result = session.query(table)
        session.close()        
        return [row.as_dict() for row in result]       
    
    def query(self, sql):
        session = self.create_session()
        result = session.execute(sql)        
        session.commit()
        key = result.keys() 
        session.close()        
        return [dict(zip(key, row)) for row in result]
          
    def add(self, sql):
        session = self.engine.connect()
        result =session.execute(sql).lastrowid
        session.commit()       
        session.close()                   
        return result
    
   
        
        
                  
        
  
        