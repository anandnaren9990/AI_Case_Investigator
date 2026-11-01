from pydantic import BaseModel

class ThresholdResponse(BaseModel):
    tshld_id: int
    aml_scenario_id : str 
    tshld_name : str 
    tshld_value : float