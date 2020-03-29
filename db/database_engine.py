from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .declarative_base import Base


class DatabaseEngine:
    DB_ENGINE = 'sqlite'
    DB_NAME = 'bug.db'

    ENGINE = create_engine('{db_engine}:///{db_name}?check_same_thread=False'.format(db_engine=DB_ENGINE, db_name=DB_NAME))
    SESSION = sessionmaker(bind=ENGINE, autoflush=False)

    def __init__(self):
        self.__engine = create_engine('{db_engine}:///{db_name}'.format(db_engine=DatabaseEngine.DB_ENGINE, db_name=DatabaseEngine.DB_NAME))

    @classmethod
    def create_tables(cls):
        Base.metadata.create_all(cls.ENGINE)

    @classmethod
    def create_session(cls):
        return cls.SESSION()
