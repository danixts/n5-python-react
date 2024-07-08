import io

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response

from app.config.container import Container
from .infraction_schema import InfractionRequest
from .infraction_service import InfractionService
from app.models.base.base_schema import ApiResponseInfraction, ApiResponseInfractionReport, ApiResponseInfractions
from app.config.dependencies import get_current_active_user
import json
import csv

from ...commons.exceptions import NotFoundError

router = APIRouter(
    prefix="/infraction",
    tags=["infraction"],
)


@router.post("", response_model=ApiResponseInfraction)
@inject
async def create_infraction(
        infraction: InfractionRequest, service: InfractionService = Depends(Provide[Container.infraction_service]),
        _=Depends(get_current_active_user)
):
    return service.create_infraction(infraction)


@router.get("/all", response_model=ApiResponseInfractions)
@inject
async def get_all_infractions_by_user(
        email: str, service: InfractionService = Depends(Provide[Container.infraction_service]),
        _=Depends(get_current_active_user)
):
    return service.generate_report(email)


@router.get("/downloadReport")
@inject
async def generate_report_by_email(
        email: str, type_report: str, response: Response,
        service: InfractionService = Depends(Provide[Container.infraction_service]),
):
    report = service.generate_report(email)
    reports_data = [report.to_dict() for report in report.data]
    response.headers["Content-Disposition"] = f"attachment; filename=Report.{type_report}"
    if type_report == "json":
        json_data = json.dumps(reports_data, indent=1)
        response.headers["Content-Type"] = "application/json"
        return json_data
    if type_report == "csv":
        response.headers["Content-Type"] = "text/csv"
        csv_data = io.StringIO()
        csv_writer = csv.DictWriter(csv_data, fieldnames=reports_data[0].keys(), delimiter="|")
        csv_writer.writeheader()
        for report in reports_data:
            csv_writer.writerow(report)
        return Response(content=csv_data.getvalue(), media_type="text/csv")
    raise NotFoundError(detail="Format not valid")
