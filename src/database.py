from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://contactsdata_user:MhW5YQ4tmtFAlGNawFIcQgNUrvvYRf0b@dpg-d8ierutckfvc73bo5cs0-a/contactsdata'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


