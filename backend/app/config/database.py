from contextlib import AbstractContextManager, contextmanager
from typing import Any, Generator
from sqlmodel import SQLModel
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import logging

log = logging.getLogger(__name__)
load_dotenv()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        SQLModel.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Generator[Any, Any, AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
