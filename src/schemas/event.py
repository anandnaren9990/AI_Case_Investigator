from pydantic import BaseModel
from datetime import datetime

class EventResponse(BaseModel):
    event_id : str 
    alert_id : str 
    event_group_id : str 
    event_group_score : float 
    reason_cd : str

class EventGroupResponse(BaseModel):
    event_group_id : str 
    event_group_name : str 
    created_at : datetime
    events : list[EventResponse]