from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://appcountacts_user:mKSLKA4oOk2Px74FB34SEyYoFGKYkaC2@dpg-d64qpivgi27c73b84bh0-a/appcountacts'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False,  bind=engine)


