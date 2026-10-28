from fastapi import  Depends, HTTPException
from src.db.models.event_model import Event, EventGroup
from src.db.session import get_event_db
from src.schemas.event import EventGroupResponse, EventResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

def get_event_details(event_group_id: str, db: Session = Depends(get_event_db)):
    try:
        statement = select(EventGroup).where(EventGroup.event_group_id==event_group_id)
        event_group_result = db.scalars(statement=statement).one_or_none()
        if event_group_result is None:
            print(f"Error in fetching event group details - {event_group_id}")
            raise HTTPException(
                status_code=404,
                detail="Event group not found"
            )
        statement1 = select(Event).where(Event.event_group_id==event_group_id)
        events_result = db.scalars(statement=statement1).all()
        if events_result is None:
            print(f"Error in fetching events details - {event_group_id}")
            raise HTTPException(
                status_code=404,
                detail="Events not found"
            )
        event_group = event_group_result
        events = events_result

        return EventGroupResponse(
            event_group_id=event_group.event_group_id,
            event_group_name=event_group.event_group_name,
            created_at=event_group.created_at,
            events=[
                EventResponse(
                    event_id=event.event_id,
                    alert_id=event.alert_id,
                    event_group_id=event.event_group_id,
                    event_group_score=event.event_group_score,
                    reason_cd=event.reason_cd
                ) for event in events
            ]
        )
    except Exception as e:
        print("Error in fetching Events")
        raise