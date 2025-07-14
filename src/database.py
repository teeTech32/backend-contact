from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contact_progresdb_user:JTOnzXib4ppVN5HCuxD8TfGBUhkonl5t@dpg-d1qh8hidbo4c73ch4f70-a/contact_progresdb'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


