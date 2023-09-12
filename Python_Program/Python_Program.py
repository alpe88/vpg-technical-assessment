import traceback

from database import open_connection, close_connection
from utils import calculate_mean, calculate_standard_deviation, find_median

from datetime import datetime, timedelta

MAX_TEMP = 0xFFFF


def InsertTemperature(temperature_reading):
    if not set(['id', 'sensor', 'name', 'temp', 'date', 'guid', 'remarks']).issubset(temperature_reading.keys()):
        print("Incomplete temperature reading data provided. Missing keys.")
        return None

    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_insert = """INSERT INTO TempReadings (id, sensor, name, temp, date, guid, remarks) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query_insert, (
            temperature_reading['id'],
            temperature_reading['sensor'],
            temperature_reading['name'],
            temperature_reading['temp'],
            temperature_reading['date'],
            temperature_reading['guid'],
            temperature_reading['remarks']
        ))

        connection.commit()

        print("Temperature reading added succesfully!")
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


def ReadTemperatures(startDate, endDate):
    readings = []

    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = "SELECT id, sensor, name, temp, date, guid, remarks FROM TempReadings"
        cursor.execute(query_select)

        readOk = True
        while readOk:
            data = cursor.fetchone()
            if data is None:
                readOk = False
                break

            if data[4] >= endDate and data[4] <= startDate:
                readings.append(data[3])

    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)

    return readings


def TemperatureStatistics(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return {
            'mean': calculate_mean(temperature_readings),
            'median': find_median(temperature_readings),
            'min': min(temperature_readings),
            'max': max(temperature_readings),
            'standard_deviation': calculate_standard_deviation(temperature_readings)
        }
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


start = datetime.now() - timedelta(days=2)
end = datetime.now()

temps = ReadTemperatures(start, end)
for t in temps:
    print(t)

temperature_statistics = TemperatureStatistics(start, end)
print(
    f"The statistics of temperature readings between our date range is: {temperature_statistics}")

temperature_reading = {
    'id': 99,
    'sensor': 'Sensor99',
    'name': 'Location99',
    'temp': 24.55,
    'date': datetime.now() - timedelta(days=1),
    'guid': 'guid99',
    'remarks': 'Remarks 99',
}
InsertTemperature(temperature_reading)
