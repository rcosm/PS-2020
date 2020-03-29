from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base
from .issue_tag import IssueTag


class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    reporter_id = Column(Integer, ForeignKey('user.id'))
    # reporter = relationship('User', back_populates='issues_reported')
    assigned_user_id = Column(Integer, ForeignKey('user.id'))
    # assigned_user = relationship('User', back_populates='issues_assigned')
    # screenshot = relationship('Screenshot', back_populates='issue')
    # tag = relationship('Tag', secondary=IssueTag, back_populates='issue')
    product_id = Column(Integer, ForeignKey('product.id'))
    # product = relationship('Product', back_populates='issue')
