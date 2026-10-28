from pydantic import BaseModel

class CustomerResponse(BaseModel):
    customer_id : str
    customer_risk : str
    customer_name : str
    customer_address : str