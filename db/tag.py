from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .declarative_base import Base
from .issue_tag import IssueTag


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # issue = relationship('Issue', secondary=IssueTag, back_populates='tag')
