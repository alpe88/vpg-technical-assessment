import traceback

from Python_Program.database import open_connection, close_connection
from Python_Program.utils import calculate_mean

from datetime import datetime, timedelta

MAX_TEMP = 0xFFFF


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


def MeanTemperature(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return calculate_mean(temperature_readings)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


def MedianTemperature(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return find_median(temperature_readings)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


def MinimumTemperature(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return min(temperature_readings)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


def MaximumTemperature(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return max(temperature_readings)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
    finally:
        close_connection(connection)


def StandardDeviation(startDate, endDate):
    try:
        connection = open_connection()
        cursor = connection.cursor()

        query_select = """SELECT temp FROM TempReadings WHERE date >= %s AND date <= %s"""
        cursor.execute(query_select, (startDate, endDate))

        temperature_readings = [row[0] for row in cursor.fetchall()]

        if not temperature_readings:
            print("No temperature readings found in the specified date range.")
            return None

        return calculate_standard_deviation(temperature_readings)
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
