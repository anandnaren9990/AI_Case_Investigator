from fastapi import APIRouter, Depends, HTTPException
from src.db.models.case_model import Case
from src.db.models.cust_model import Customer
from src.db.session import get_case_db,get_case_cust_db,get_event_db,get_aml_db
from src.schemas.case import CaseCustomerEventAlertResponse
from src.schemas.cust import CustomerResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.services.event import get_event_details
from src.services.alert import get_alert_details

router = APIRouter(
    prefix="/cases",
    tags=["Cases"]
)

@router.get("/{case_id}")
def get_case_details(case_id: str, db1: Session = Depends(get_case_db), db2: Session = Depends(get_case_cust_db), db3: Session = Depends(get_event_db), db4: Session = Depends(get_aml_db)):
    try:
        statement1 = select(Case).where(Case.case_id==case_id)
        result1 = db1.scalars(statement1).one_or_none()
                
        if result1 is None:
            raise HTTPException(
                status_code=404,
                detail="Case not found"
                )
        case = result1
        statement2 = select(Customer).where(Customer.customer_id==case.focus_entity)
        result2 = db2.scalars(statement2).one_or_none()
        cust = result2
        if result2 is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
                )
        event_group_details = get_event_details(event_group_id=case.event_group_id, db=db3)

        alert_ids = [event.alert_id for event in event_group_details.events]

        alert_details = get_alert_details(alert_ids=alert_ids, db=db4)

        output =  CaseCustomerEventAlertResponse(
            case_id=case.case_id,
            focus_entity=case.focus_entity,
            event_group_id=case.event_group_id,
            overall_risk=case.overall_risk,
            customer=CustomerResponse(
                customer_id=cust.customer_id,
                customer_name=cust.customer_name,
                customer_risk=cust.customer_risk,
                customer_address=cust.customer_address
                ),
            event=event_group_details,
            alerts=alert_details
            )
        return output
    except Exception as e:
        print(f"Exception occured {e}")
        raise