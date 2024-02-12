from datetime import datetime, timedelta
import random

# Adding argument parsing 
import argparse

# OS traversal 
import os 

# PSQL connection 
import psycopg2

# Loading the .env 
from dotenv import load_dotenv

# Iteration tracking 
from tqdm import tqdm

# Getting the current path 
current_path = os.path.dirname(os.path.abspath(__file__))

# Loading the .env file from a dir above
load_dotenv(dotenv_path=os.path.join(current_path, "..", ".env"))

# Getting the environment variables
db_user = os.getenv('PSQL_USER', 'default_user')
db_pass = os.getenv('PSQL_PASSWORD', 'default_pass')
db_host = os.getenv('PSQL_HOST', 'localhost')
db_name = os.getenv('PSQL_DATABASE', 'default_db')
db_port = os.getenv('PSQL_PORT', '5432')

# Creating a dictionary to adjust the ranges for every device id 
device_ranges = {
    1: 1.0, 
    2: 1.2,
    3: 1.3,
    4: 1.4,
    5: 1.5
}

def generate_minute_level_mock_data(start_date, end_date, device_id, metric):
    """
    Generates mock data for specified device_id and metric, following a daily usage pattern,
    with data points at minute-level granularity between start and end dates.
    
    :param start_date: The start date for data generation (datetime.date object).
    :param end_date: The end date for data generation (datetime.date object).
    :param device_id: The device ID for which to generate the data.
    :param metric: The metric name, e.g., "power_usage".
    :return: A list of data points, each with a timestamp, device_id, metric, and value.
    """
    mock_data = []
    delta = timedelta(days=1)
    current_date = start_date
    
    high_range = (50, 70)  # High usage value range
    medium_range = (30, 50)  # Medium usage value range
    low_range = (10, 30)  # Low usage value range
    
    while current_date <= end_date:
        for hour in range(24):
            for minute in range(0, 60, 1):  # Generate data every minute
                timestamp = datetime(current_date.year, current_date.month, current_date.day, hour, minute)
                if 6 <= hour < 10 or 18 <= hour < 22:
                    value = random.uniform(*high_range)
                elif 10 <= hour < 18:
                    value = random.uniform(*medium_range)
                else:
                    value = random.uniform(*low_range)
                
                mock_data.append({
                    "timestamp": timestamp.strftime('%Y-%m-%d %H:%M'),
                    "device_id": device_id,
                    "metric": metric,
                    "value": value * device_ranges[device_id],
                    "created_datetime": datetime.now(),
                    "updated_datetime": datetime.now(),
                })
        current_date += delta
    
    return mock_data

def upsert_data(connection, data):
    """
    Inserts or updates data in the database based on the existence of a row with the same
    timestamp, device_id, and metric.
    
    :param connection: An active psycopg2 connection to the PostgreSQL database.
    :param data: A dictionary containing the data to insert or update.
    """
    cursor = connection.cursor()
    
    # SQL for updating an existing row
    update_sql = """
    UPDATE timeseries
    SET value = %s, updated_datetime = %s
    WHERE timestamp = %s AND device_id = %s AND metric = %s;
    """
    
    # SQL for inserting a new row
    insert_sql = """
    INSERT INTO timeseries (timestamp, device_id, metric, value, created_datetime, updated_datetime)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    # SQL for checking if a row exists
    check_sql = """
    SELECT 1
    FROM timeseries
    WHERE timestamp = %s AND device_id = %s AND metric = %s;
    """

    for entry in tqdm(data):
        # Checking if exists 
        cursor.execute(check_sql, (entry['timestamp'], entry['device_id'], entry['metric']))

        # If exists, update the row
        if cursor.fetchone():
            cursor.execute(update_sql, (entry['value'], entry['updated_datetime'], entry['timestamp'], entry['device_id'], entry['metric']))
        else:
            cursor.execute(insert_sql, (entry['timestamp'], entry['device_id'], entry['metric'], entry['value'], entry['created_datetime'], entry['updated_datetime']))

        # Commit the changes
        connection.commit()
    cursor.close()

if __name__ == '__main__': 
    # Parsing the arguments for the mocking function 
    parser = argparse.ArgumentParser(description='Mocking data for the power usage')

    parser.add_argument('--start_date', type=str, help='The start date for data generation (datetime.date object).')
    parser.add_argument('--end_date', type=str, help='The end date for data generation (datetime.date object).')
    parser.add_argument('--device_id', type=int, help='The device ID for which to generate the data.')
    parser.add_argument('--metric', type=str, help='The metric name, e.g., "power_usage".')

    args = parser.parse_args()

    # Converting to dates
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date()

    mock_data = generate_minute_level_mock_data(start_date, end_date, args.device_id, args.metric)

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
        database=db_name
        )
    
    # Upsert the mock data into the database
    upsert_data(connection, mock_data)