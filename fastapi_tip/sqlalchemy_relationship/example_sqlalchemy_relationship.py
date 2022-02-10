'''
참고: https://weejw.tistory.com/84
'''
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy  import  Column, ForeignKey , Integer 
from sqlalchemy.orm import relationship

'''
setdb
'''

DATABASE_URL = 'YOURDBURL'
engine = create_engine(DATABASE_URL , echo =True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
Declare db model
'''
#1:N 관계 (user - blog 관계)
#한 유저(1)는 여러개의 글(N)을 쓸 수 있다
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


#2.N:1 관계
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child")

#1:1 관계 (member -address 관계)
#back_populates:
#relationship.backref 또는 relationship.back_populates로 양방향으로 설정할 수 있다
#uselist : 참조 무결성을 위함
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent = relationship("Parent", back_populates="child", uselist=False)



#4.N:M 관계
#association_table을 추가하여 두 테이블을 연결시켜준다.
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",secondary=association_table)

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

#cf casecade : 외래키 설정시 종속 조건을 주어 외래키가 삭제되면 같이 삭제
class Votes(Base):
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("user.id" , ondelete= "CASECADE") , primary_key= True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete= "CASECADE") , primary_key= True)