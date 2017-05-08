#! /usr/bin/python3
# @Djavan Sergent
import dbmanager as db
from sqlalchemy import Column, Integer, Sequence, String, exists
from sqlalchemy.orm import relationship


class User(db.Base):
    """
    A Mapping class for User Objects
    """
    __tablename__ = 'user'

    # Table fields
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(Integer, nullable=False)
    pictures = relationship('Video', secondary='video_user_link')

    def exist(self, session):
        """
        :param session: database transaction session
        :return: Boolean - False if not in database
        """
        return session.query(exists().where(User.name == self.name)).scalar()

    def __repr__(self):
        return "<User(id='%s', name='%s')>" \
               % (self.id, self.name)
