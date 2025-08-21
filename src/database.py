from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactadb_user:5CdljSJIDAI5dSo6ATsuqwGTA2MymVzx@dpg-d2is7aemcj7s73cqdu4g-a/contactadb'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


