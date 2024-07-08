from dependency_injector import containers, providers
from app.config.database import Database
from app.config.config import Configs
from app.models.infraction.infraction_repository import InfractionRepository
from app.models.infraction.infraction_service import InfractionService
from app.models.police.police_repository import PoliceRepository
from app.models.user.user_repository import UserRepository
from app.models.vehicle.vehicle_repository import VehicleRepository
from app.models.auth.auth_service import AuthService
from app.models.user.user_service import UserService
from app.models.vehicle.vehicle_service import VehicleService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.models.auth.auth_controller",
            "app.models.user.user_controller",
            "app.models.vehicle.vehicle_controller",
            "app.models.infraction.infraction_controller",
            "app.config.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=Configs.DATABASE_URI)
    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )
    auth_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )
    vehicle_repository = providers.Factory(
        VehicleRepository, session_factory=db.provided.session
    )
    police_repository = providers.Factory(
        PoliceRepository, session_factory=db.provided.session
    )
    infraction_repository = providers.Factory(
        InfractionRepository, session_factory=db.provided.session
    )
    user_service = providers.Factory(UserService, user_repository=user_repository, police_repository=police_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    vehicle_service = providers.Factory(VehicleService, vehicle_repository=vehicle_repository)
    infraction_service = providers.Factory(InfractionService, infraction_repository=infraction_repository,
                                           police_repository=police_repository)
