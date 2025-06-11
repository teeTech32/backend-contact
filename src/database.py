from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://contactdb_ptxk_user:YNaAfaXEPcXW7xaHURTPIe0mwdW695w5@dpg-d148tv15pdvs73bafteg-a/contactdb_ptxk'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


