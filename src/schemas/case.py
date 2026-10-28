from pydantic import BaseModel
from src.schemas.cust import CustomerResponse
from src.schemas.event import EventGroupResponse
from src.schemas.alert import AlertResponse

class CaseResponse(BaseModel):
    case_id : str
    focus_entity : str
    event_group_id : str
    overall_risk : str

class CaseCustomerEventAlertResponse(BaseModel):
    case_id : str
    focus_entity : str
    event_group_id : str
    overall_risk : str
    customer : CustomerResponse
    event : EventGroupResponse
    alerts : list[AlertResponse]