from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contacts_db_ix25_user:nEtTcslmA04VJEZDB0LpDTJJy2oXSr66@dpg-d44ik5ali9vc73bm5060-a/contacts_db_ix25'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


