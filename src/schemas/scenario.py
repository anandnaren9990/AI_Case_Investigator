from pydantic import BaseModel

class Scenario(BaseModel):
    aml_scenario_id : str 
    aml_scenario_name : str 
    aml_scenario_short_description : str 
    aml_scenario_description : str