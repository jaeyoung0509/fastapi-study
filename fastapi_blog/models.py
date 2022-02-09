from sqlalchemy  import TIMESTAMP, Column, ForeignKey , Integer , String  , Boolean 
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer , primary_key= True)
    title = Column(String , nullable= False)
    content = Column(String , nullable= False)
    published = Column(Boolean , server_default= 'TRUE' , nullable= False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer ,ForeignKey ("user.id" , ondelete="CASCADE") , nullable= False)
    owner = relationship("User")
class User(Base):
    __tablename__ = "user"
    id = Column(Integer , primary_key= True , nullable= False)
    email =Column(String , nullable= True , unique= True )
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Votes(Base):
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("user.id" , ondelete= "CASECADE") , primary_key= True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete= "CASECADE") , primary_key= True)