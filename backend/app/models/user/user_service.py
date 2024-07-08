from app.models.base.base_service import BaseService
from app.models.user.user_repository import UserRepository
from .user_schema import UserModel, UserUpdate
from app.commons.exceptions import NotFoundError, SuccessResponse
from app.commons.security import get_password_hash
from app.models.police.police_repository import PoliceRepository
from ..police.police_entity import PoliceEntity


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository, police_repository: PoliceRepository):
        self.user_repository = user_repository
        self.police_repository = police_repository
        super().__init__(user_repository)

    def create_user(self, user: UserModel):
        if user.type not in ["user", "policy"]:
            raise NotFoundError(detail="User type not valid", cod_error="COD001")
        find_user = self.user_repository.get_user_by_user(user.email or user.username)
        if find_user:
            raise NotFoundError(detail="User already exists", cod_error="COD001")
        if user.type == "policy":
            find_policy = self.police_repository.get_policy(user.name, user.code_officer)
            if find_policy:
                raise NotFoundError(detail="Error create official", cod_error="COD001")
        user.password = get_password_hash(user.password)
        create_user = self.user_repository.create(user)
        if user.type == "policy":
            if user.name and user.code_officer:
                new_policy = PoliceEntity()
                new_policy.name = user.name
                new_policy.user_id = create_user.id
                new_policy.code_officer = user.code_officer
                self.police_repository.create(new_policy)
            else:
                self.delete_user(create_user.id)
                raise NotFoundError(detail="name and code_officer is required", cod_error="COD002")
        return SuccessResponse(create_user)

    def find_by_email_or_username(self, email_or_user: str):
        find_user = self.user_repository.get_user_by_user(email_or_user)
        if find_user:
            return SuccessResponse(find_user)
        raise NotFoundError(detail="User not found", cod_error="COD002")

    def find_by_all(self):
        users = self.user_repository.find_by_all()
        return SuccessResponse(users)

    def update_user(self, user_id: int, body: UserUpdate):
        user_found = self.user_repository.read_by_id(user_id)
        if not user_found:
            raise NotFoundError(detail="User not found", cod_error="COD002")
        if user_found.email == body.email:
            raise NotFoundError(detail="User email not change", cod_error="COD004")
        body.password = get_password_hash(body.password)
        update_user = self.user_repository.update(user_id, body)
        if update_user:
            return SuccessResponse(update_user)
        raise NotFoundError(detail="User not found", cod_error="COD003")

    def delete_user(self, user_id: int):
        user = self.user_repository.delete_by_id(user_id)
        return SuccessResponse(user)
