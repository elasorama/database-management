from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Timeseries(Base):
    """
    Class for the timeseries table; This is the data that is aggregated to minutes from the raw data 
    stream.
    """
    __tablename__ = 'timeseries'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer)
    metric = Column(String)
    value = Column(Float)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)


class ApiLogs(Base):
    """
    Class for the api_logs table; This is the data that is aggregated to minutes from the raw data 
    stream.
    """
    __tablename__ = 'api_logs'
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    deployment = Column(String)
    timestamp = Column(DateTime)
    device_id = Column(Integer)
    metric = Column(String)
    n_ahead = Column(Integer) # Minutes ahead for aggregates
    value = Column(Float)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)
    response_status_code = Column(Integer)