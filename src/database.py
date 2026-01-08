from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactapplication_3spf_user:8sHOt1ZF5x945XxfATePYxIVlq2wZode@dpg-d5fj64vpm1nc73deqlug-a/contactapplication_3spf'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


