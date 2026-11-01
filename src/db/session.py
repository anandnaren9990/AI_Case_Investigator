import os
from collections.abc import Generator
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()

def get_var(var_name: str) -> str:
    var_value = os.getenv(var_name)
    if not var_value:
        raise RuntimeError(f"Env variable missing: {var_name}")
    return var_value

def create_db_url(
        db_name: str, 
        db_user : str,
        db_pass : str
    ) -> URL:
    return URL.create(
        drivername='mysql+pymysql',
        username=get_var(db_user),
        password=get_var(db_pass),
        host=get_var('DB_HOST'),
        port=int(get_var('DB_PORT')),
        database=get_var(db_name)
    )

case_engine = create_engine(
    url=create_db_url(
        'CASE_DB_NAME',
        'CASE_DB_USER',
        'CASE_DB_PASSWORD'
    ),
    pool_pre_ping=True,
    pool_recycle=1800
)

case_cust_engine = create_engine(
    url=create_db_url(
        'CUST_DB_NAME',
        'CASE_DB_USER',
        'CASE_DB_PASSWORD'
    ),
    pool_pre_ping=True,
    pool_recycle=1800
)

aml_engine = create_engine(
    url=create_db_url(
        'AML_DB_NAME',
        'AML_DB_USER',
        'AML_DB_PASSWORD'
    ),
    pool_pre_ping=True,
    pool_recycle=1800
)

event_engine = create_engine(
    url=create_db_url(
        'EVENT_DB_NAME',
        'EVENT_DB_USER',
        'EVENT_DB_PASSWORD'
    ),
    pool_pre_ping=True,
    pool_recycle=1800
)

aml_cust_engine = create_engine(
    url=create_db_url(
        'CUST_DB_NAME',
        'AML_DB_USER',
        'AML_DB_PASSWORD'
    ),
    pool_pre_ping=True,
    pool_recycle=1800
)

CaseSessionLocal = sessionmaker(
    bind=case_engine,
    autoflush=False,
    expire_on_commit=False
)

CaseCustSessionLocal = sessionmaker(
    bind=case_cust_engine,
    autoflush=False,
    expire_on_commit=False
)

AmlSessionLocal = sessionmaker(
    bind=aml_engine,
    autoflush=False,
    expire_on_commit=False
)

AmlCustSessionLocal = sessionmaker(
    bind=aml_cust_engine,
    autoflush=False,
    expire_on_commit=False
)

EventSessionLocal = sessionmaker(
    bind=event_engine,
    autoflush=False,
    expire_on_commit=False
)

def get_case_db() -> Generator[Session, None, None]:
    db = CaseSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_case_cust_db() -> Generator[Session, None, None]:
    db = CaseCustSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_event_db() -> Generator[Session, None, None]:
    db = EventSessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_aml_db() -> Generator[Session, None, None]:
    db = AmlSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_aml_cust_db() -> Generator[Session, None, None]:
    db = AmlCustSessionLocal()
    try:
        yield db
    finally:
        db.close()