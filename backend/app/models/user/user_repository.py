from contextlib import AbstractContextManager
from typing import Callable
from app.models.base.base_repository import BaseRepository
from sqlalchemy.orm import Session
from app.models.user.user_entity import UserEntity


class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, UserEntity)

    def get_user_by_user(self, username: str):
        with self.session_factory() as session:
            query = (
                session.query(self.model)
                .filter(
                    ((self.model.username == username) | (self.model.email == username))
                    & self.model.is_active
                )
                .first()
            )
        return query

    def find_by_all(self):
        with self.session_factory() as session:
            return session.query(self.model)
