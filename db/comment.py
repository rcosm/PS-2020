from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, ForeignKey('issue.id'))
    # issue = relationship('Issue', back_populates='comment')
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship('User', back_populates='comment')
    message = Column(String)
    