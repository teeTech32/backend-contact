from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://teecontact_user:m2JhYkTz496FM7KzjeVVArG0tAWl8pY8@dpg-d7r0p7hkh4rs73eidrp0-a/teecontact'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


