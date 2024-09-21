from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from directories.constants.c_directories import DB, DIRS


def get_db_engine():
    db_path: str = DIRS.paths[DB]
    engine: Engine = create_engine(f"sqlite:///{db_path}", echo=False)
    return engine


def create_session():
    ENGINE = get_db_engine()
    Session = sessionmaker(bind=ENGINE)
    session = Session()

    return session


BASE = declarative_base()
