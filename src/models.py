import os
import sys, enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Medias(enum.Enum):
    one = "facebook"
    two = "twitter"
    three = "instagram"

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key = True, nullable=False)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key = True, nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key = True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    user = relationship(User)

class Comment(Base):
    __tablename__ = "comment"
    ID = Column(Integer, primary_key = True, nullable=False)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.ID'), nullable=False)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.ID'), nullable=False)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key = True, nullable=False)
    type = Column(Enum(Medias), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.ID'), nullable=False)
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
