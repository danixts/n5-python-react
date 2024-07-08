from contextlib import AbstractContextManager
from typing import Any, Callable, Type, TypeVar

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app.commons.exceptions import DuplicatedError, NotFoundError
from app.models.base.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository:
    def __init__(
            self,
            session_factory: Callable[..., AbstractContextManager[Session]],
            model: Type[T],
    ) -> None:
        self.session_factory = session_factory
        self.model = model

    def read_by_id(self, id: int, eager: bool = False):
        with self.session_factory() as session:
            query = session.query(self.model)
            if eager:
                for eager in getattr(self.model, "eagers", []):
                    query = query.options(joinedload(getattr(self.model, eager)))
            query = query.filter(self.model.id == id).first()
            if not query:
                raise NotFoundError(detail=f"not found id : {id}")
            return query

    def create(self, schema: T):
        with self.session_factory() as session:
            query = self.model(**schema.model_dump())
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(detail="Duplicate Value")
            return query

    def update(self, id: int, schema: T):
        with self.session_factory() as session:
            db_update = session.get(self.model, id)
            if not db_update:
                raise NotFoundError("ELEMENT NOT FOUND")
            model_date = schema.model_dump(exclude_unset=True)
            db_update.sqlmodel_update(model_date)
            session.add(db_update)
            session.commit()
            session.refresh(db_update)
            return db_update

    def update_attr(self, id: int, column: str, value: Any):
        with self.session_factory() as session:
            session.query(self.model).filter(self.model.id == id).update(
                {column: value}
            )
            session.commit()
            return self.read_by_id(id)

    def whole_update(self, id: int, schema: T):
        with self.session_factory() as session:
            session.query(self.model).filter(self.model.id == id).update(
                schema.model_dump()
            )
            session.commit()
            return self.read_by_id(id)

    def delete_by_id(self, id: int):
        with self.session_factory() as session:
            query = session.get(self.model, id)
            if not query:
                raise NotFoundError(detail=f"Not found id: {id}")
            session.delete(query)
            session.commit()
            return query
