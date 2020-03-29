from sqlalchemy import Table, Column, ForeignKey
from .declarative_base import Base


IssueTag = Table('issue_tag', Base.metadata,
                Column('issue_id', ForeignKey('issue.id'), primary_key=True),
                Column('tag_id', ForeignKey('tag.id'), primary_key=True)
            )