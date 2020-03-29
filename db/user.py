from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    # issues_reported = relationship('Issue', back_populates='reporter', foreign_keys='Issue.reporter_id')
    # issues_assigned = relationship('Issue', back_populates='assigned_user', foreign_keys='issue.assigned_user_id')
    