from fastapi import  Depends, HTTPException
from src.db.models.alert_model import Alert
from src.db.session import get_aml_db
from src.schemas.alert import AlertResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

def get_alert_details(alert_ids: list, db: Session = Depends(get_aml_db)):
    try:
        unique_alert_ids = list(dict.fromkeys(alert_ids))
        statement = select(Alert).where(Alert.alert_id.in_(unique_alert_ids))
        alert_result = db.scalars(statement=statement).all()
        if alert_result is None:
            print(f"Error in fetching alert details - {alert_ids}")
            raise HTTPException(
                status_code=404,
                detail="Alerts not found"
            )
        alerts = alert_result
        return [
            AlertResponse(
                alert_id=alert.alert_id,
                focus_entity=alert.focus_entity,
                aml_scenario_id=alert.aml_scenario_id,
                highlights=alert.highlights
            ) for alert in alerts
        ]
    except Exception as e:
        print("Error in fetching Events")
        raise