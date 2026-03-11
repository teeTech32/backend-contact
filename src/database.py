from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://mycountactapp_user:3et8aIigBRslSrggudjJ0ILHO5Xdxyby@dpg-d6ouh5n5gffc738qb93g-a/mycountactapp'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


