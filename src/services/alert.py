from fastapi import  Depends, HTTPException
from src.db.models.alert_model import Alert
from src.db.models.cust_model import Customer
from src.db.models.scenario_model import Scenario
from src.db.models.threshold_model import Threshold
from src.db.session import get_aml_db, get_aml_cust_db
from src.schemas.alert import AlertResponse,AlertPayloadResponse
from src.schemas.threshold import ThresholdResponse
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_alert_details(alert_ids: list, db: Session = Depends(get_aml_db)):
    try:
        unique_alert_ids = list(dict.fromkeys(alert_ids))
        statement = select(Alert,Scenario).join(Scenario,Alert.aml_scenario_id==Scenario.aml_scenario_id).where(Alert.alert_id.in_(unique_alert_ids))
        alert_result = db.execute(statement=statement).all()
        if alert_result is None:
            print(f"Error in fetching alert details - {alert_ids}")
            raise HTTPException(
                status_code=404,
                detail="Alerts not found"
            )
        return [
            AlertResponse(
                alert_id=alert.alert_id,
                focus_entity=alert.focus_entity,
                aml_scenario_id=alert.aml_scenario_id,
                highlights=alert.highlights,
                scenario_name=scen.aml_scenario_name,
                scenario_desc=scen.aml_scenario_description
            ) for alert, scen in alert_result
        ]
    except Exception as e:
        print("Error in fetching alerts")
        raise

def get_alert_scen_details(alert_id: list, db1: Session = Depends(get_aml_db), db2: Session = Depends(get_aml_cust_db)):
    try: 
        statement1 = select(Alert).where(Alert.alert_id==alert_id)
        result1 = db1.scalars(statement=statement1).one_or_none()
        if result1 is None:
            print(f"No alert found with alert id - {alert_id}")
            raise HTTPException(
                status_code=404,
                detail="Alert id not found"
            )
        alert_details = result1
        statement2 = select(Customer).where(Customer.customer_id==alert_details.focus_entity)
        result2 = db2.scalars(statement=statement2).one_or_none()
        if result2 is None:
            print(f"No customer found for customer id - {alert_details.focus_entity}")
            raise HTTPException(
                status_code=404,
                detail="Customer Id not found."
            )
        cust_details = result2
        statement3 = select(Scenario).where(Scenario.aml_scenario_id==alert_details.aml_scenario_id)
        result3 = db1.scalars(statement=statement3).one_or_none()
        if result3 is None:
            print(f"No Scenario found for scenario id - {alert_details.aml_scenario_id}")
            raise HTTPException(
                status_code=404,
                detail="Scenario Id not found."
                )
        scen_details = result3
        statement4 = select(Threshold).where(Threshold.aml_scenario_id==scen_details.aml_scenario_id)
        result4 = db1.scalars(statement=statement4).all()
        if result4 is None:
            print(f"No Threshold found for scenario id - {scen_details.aml_scenario_id}")
            raise HTTPException(
                status_code=404,
                detail="Thresholds not found."
                )
        tshld_details = result4
        alert_payload =  AlertPayloadResponse(
            alert_id=alert_details.alert_id,
            focus_entity=alert_details.focus_entity,
            aml_scenario_id=alert_details.aml_scenario_id,
            highlights=alert_details.highlights,
            customer_risk=cust_details.customer_risk,
            scenario_name=scen_details.aml_scenario_name,
            scenario_desc=scen_details.aml_scenario_description,
            thresholds=[ThresholdResponse(
                tshld_id=tshld.tshld_id,
                aml_scenario_id=tshld.aml_scenario_id,
                tshld_name=tshld.tshld_name,
                tshld_value=tshld.tshld_value
            ) for tshld in tshld_details ]
        )
        return alert_payload
    except Exception as e:
        print(f"Error fetching alert details")
        raise

