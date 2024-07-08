from contextlib import AbstractContextManager
from typing import Callable
from app.models.base.base_repository import BaseRepository
from sqlalchemy.orm import Session
from app.models.infraction.infraction_entity import InfractionEntity
from sqlalchemy import text


class InfractionRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, InfractionEntity)

    def get_report_email(self, email):
        with self.session_factory() as session:
            try:
                result = session.execute(text(f"select * from public.sp_get_report_by_email('{email}');"))
                return result.fetchall()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                session.close()

    def get_infraction_by_all_user(self, policy_id: int):
        with self.session_factory() as session:
            query = session.query(self.model).filter(self.model.police_id == policy_id)
            return query
