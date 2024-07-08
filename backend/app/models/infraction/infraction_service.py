from app.commons.exceptions import SuccessResponse, NotFoundError
from app.commons.strings import is_valid_email
from app.models.base.base_service import BaseService
from app.models.infraction.infraction_entity import InfractionEntity
from app.models.infraction.infraction_repository import InfractionRepository
from app.models.infraction.infraction_schema import InfractionRequest, ReportModel
from app.models.police.police_entity import PoliceEntity
from app.models.police.police_repository import PoliceRepository


class InfractionService(BaseService):
    def __init__(self, infraction_repository: InfractionRepository, police_repository: PoliceRepository):
        self.infraction_repository = infraction_repository
        self.police_repository = police_repository
        super().__init__(infraction_repository)

    def create_infraction(self, body: InfractionRequest):
        policy = self.police_repository.get_policy_user_id(body.police_id)
        infraction = InfractionEntity()
        infraction.police_id = policy.id
        infraction.comments = body.comments
        infraction.state = body.state
        infraction.timestamp = body.timestamp
        infraction.vehicle_id = body.vehicle_id
        create_infraction = self.infraction_repository.create(infraction)
        return SuccessResponse(create_infraction)

    def generate_report(self, email):
        if not is_valid_email(email):
            raise NotFoundError(cod_error="COD005", detail='Invalid no valid')
        reports = self.infraction_repository.get_report_email(email)
        if len(reports) == 0:
            raise NotFoundError(detail="NOT INFRACTIONS", cod_error="COD101")
        infraction_report = [ReportModel(*report) for report in reports]
        return SuccessResponse(infraction_report)

    def get_infraction_by_user(self, user_id):
        policy = self.police_repository.get_policy_user_id(user_id)
        return SuccessResponse(self.infraction_repository.get_infraction_by_all_user(policy.id))
