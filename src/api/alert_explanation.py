from fastapi import APIRouter, Depends, HTTPException
from src.db.session import get_aml_db, get_aml_cust_db
from src.services.llm_explanation import generate_llm_response
from src.services.alert import get_alert_scen_details
from src.logic.scen_logic import get_scen_logic
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

@router.post("/{alert_id}/explain")
def get_alert_exp(alert_id: str, db1: Session = Depends(get_aml_db), db2: Session = Depends(get_aml_cust_db)):
    alert_payload_response = get_alert_scen_details(alert_id=alert_id, db1=db1, db2= db2)
    if alert_payload_response is None:
        print(f"Error in fetching alert details of alert id - {alert_id}")
        raise HTTPException(
            status_code=500,
            detail="Alert details could not be fetched"
        )
    scen_id = alert_payload_response.aml_scenario_id
    scen_logic = get_scen_logic(scenario_id=scen_id)
    llm_payload = {
        "alert_details": alert_payload_response.model_dump(mode="json"),
        "scenario_logic": scen_logic
    }
    llm_explanation = generate_llm_response(alert_payload=llm_payload)
    if llm_explanation is None:
        print(f"Error in generating LLM explanation")
        raise HTTPException(
            status_code=404,
            detail="Unable to generate LLM explanation"
        )
    alert_explanation = llm_explanation.json()["message"]["content"]
    return alert_explanation
        