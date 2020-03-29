from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Screenshot(Base):
    __tablename__ = 'screenshot'

    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, ForeignKey('issue.id'))
    path_to_screenshot = Column(String)
    # issue = relationship('Issue', back_populates='screenshot')
