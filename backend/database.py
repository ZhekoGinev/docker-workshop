from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DATABASE_URL = f"mysql+pymysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@mariadb/currencies"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    abbreviation = Column(String)
    value_in_bgn = Column(Float)

    def __init__(self, name, abbreviation, value_in_bgn):
        self.name = name
        self.abbreviation = abbreviation
        self.value_in_bgn = value_in_bgn
