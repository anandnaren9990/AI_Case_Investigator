from typing import Any
from pydantic import BaseModel
from src.schemas.threshold import ThresholdResponse

class AlertResponse(BaseModel):
    alert_id : str 
    focus_entity : str 
    aml_scenario_id : str 
    highlights : dict[str, Any]
    scenario_name : str
    scenario_desc : str

class AlertPayloadResponse(BaseModel):
    alert_id : str 
    focus_entity : str 
    aml_scenario_id : str 
    highlights : dict[str, Any]
    customer_risk : str
    scenario_name : str
    scenario_desc : str
    thresholds : list[ThresholdResponse]