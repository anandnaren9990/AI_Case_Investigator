from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.session import case_engine, aml_engine, event_engine

def verify_engine(name, engine):
    try:
        with engine.connect() as connection:
            result = connection.execute(text('select 2')).scalar_one()
            if result==2:
                print(f"DB {name} connected successfully")
    except SQLAlchemyError:
        print(f"{name} DB connection failure")
        raise

verify_engine("CASE_DB", case_engine)
verify_engine("EVENT_DB", event_engine)
verify_engine("AML_DB", aml_engine)