from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactsdatab_user:3V7Dy6ekrmCQ72PSkiQQsIg8NrPt7oK9@dpg-d36n2kvfte5s73bkrgdg-a/contactsdatab'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


