from contextlib import AbstractContextManager
from typing import Callable

from app.commons.exceptions import NotFoundError
from app.models.base.base_repository import BaseRepository
from sqlalchemy.orm import Session
from app.models.police.police_entity import PoliceEntity


class PoliceRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, PoliceEntity)

    def get_policy(self, name: str, code: int):
        with self.session_factory() as session:
            query = (
                session.query(self.model)
                .filter(
                    (self.model.name == name) | (self.model.code_officer == str(code))
                )
                .first()
            )
        return query

    def get_policy_user_id(self, user_id: int):
        with self.session_factory() as session:
            policy = session.query(self.model).filter(self.model.user_id == user_id).first()
            if policy:
                return policy
            raise NotFoundError(detail="NOT FOUND USER")
