from database import open_connection, close_connection
from datetime import datetime, timedelta

import traceback

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


start = datetime.now() - timedelta(days=2)
end = datetime.now()

temps = ReadTemperatures(start, end)
for t in temps:
    print(t)
