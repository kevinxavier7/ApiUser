from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()

class Base(BaseModel):
    __abstract__ = True
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    