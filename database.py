from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from password import pg_user, pg_port, pg_host, password, db_name


engine = create_engine(f'postgresql://{pg_user}:{password}@{pg_host}:{pg_port}/{db_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
