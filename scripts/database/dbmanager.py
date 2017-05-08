#! /usr/bin/python3
# @Djavan Sergent
# See http://docs.sqlalchemy.org/en/latest/orm/tutorial.html for more details about SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Database engine and session parameters
Base = declarative_base()
engine = create_engine('sqlite:///../../data/ima.db', echo=False)  # echo = logging in console
Session = sessionmaker(bind=engine)

# Classes which needed a Base, no on top import
from video import Video
from user import User
from videouserlink import VideoUserLink  # Used for table creation ! do not delete this line !
