from typing import Any
from pydantic import BaseModel

class AlertResponse(BaseModel):
    alert_id : str 
    focus_entity : str 
    aml_scenario_id : str 
    highlights : dict[str, Any]