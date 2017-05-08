#! /usr/bin/python3
# @Djavan Sergent
import dbmanager as db
from sqlalchemy import Column, Integer, ForeignKey


class VideoUserLink(db.Base):
    """
    A mapping class for link between Video and User Object
    which contains an evaluation
    """
    __tablename__ = 'video_user_link'

    # Table fields
    video_id = Column(Integer, ForeignKey('video.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    grade = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Link(vid='%s', uid='%s')>" \
               % (self.video_id, self.user_id)

