#! /usr/bin/python3
# @Djavan Sergent
import dbmanager as db
from sqlalchemy import Column, Integer, String, Sequence, exists
from sqlalchemy.orm import relationship
from user import User


class Video(db.Base):
    """
    A Mapping class for Video Objects
    """
    __tablename__ = 'video'

    # Table fields
    id = Column(Integer, Sequence('video_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    users = relationship(User, secondary='video_user_link')

    def exist(self, session):
        """
        :param session: database transaction session
        :return: Boolean - False if not in database
        """
        return session.query(exists().where(Video.name == self.name)).scalar()

    def __repr__(self):
        return "<Video(id='%s', name='%s')>" \
               % (self.id, self.name)