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


class TimeseriesAggregated(Base):
    """
    Class for the timeseries_aggregated table; This is the data that is aggregated to minutes from the raw data 
    stream.
    """
    __tablename__ = 'timeseries_aggregated'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer)
    metric = Column(String)
    n_ahead = Column(Integer) # Minutes ahead for aggregates 
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
    request = Column(String)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)
    response_status_code = Column(Integer)


class PowerConsumption(Base):
    """
    Class for the power_consumption table;
    This is the data table that stores the 
    aggregates from the historical data where for each timestep, 
    the true comsumption for the next 5 minutes, 15 minutes and 60 minutes
    are stored
    """
    __tablename__ = 'power_consumption'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    power_usage_5_minutes_ahead = Column(Float, nullable=True)
    power_usage_15_minutes_ahead = Column(Float, nullable=True)
    power_usage_60_minutes_ahead = Column(Float, nullable=True)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)


class ApiPowerUsage(Base): 
    """
    Class for the api_usage table;
    This is the data table that stores the 
    aggregates from the historical data where for each timestep, 
    the true comsumption for the next 5 minutes, 15 minutes and 60 minutes
    are stored
    """
    __tablename__ = 'api_power_usage'
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    version = Column(String)
    timestamp = Column(DateTime)
    request = Column(String)
    power_usage_5_minutes_ahead = Column(Float)
    power_usage_15_minutes_ahead = Column(Float)
    power_usage_60_minutes_ahead = Column(Float)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)
    response_status_code = Column(Integer)


class ApiPowerUsageAnalytics(Base): 
    """
    Table used in analytics to store the results of the api usage
    """
    __tablename__ = 'api_power_usage_analytics'
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    version = Column(String)
    timestamp = Column(DateTime)
    power_usage_5_minutes_ahead = Column(Float)
    power_usage_15_minutes_ahead = Column(Float)
    power_usage_60_minutes_ahead = Column(Float)
    power_usage_5_minutes_ahead_forecast = Column(Float)
    power_usage_15_minutes_ahead_forecast = Column(Float)
    power_usage_60_minutes_ahead_forecast = Column(Float)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)