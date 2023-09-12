from django.conf import settings
from datetime import datetime, date, time, timedelta
import psycopg2


MAX_TEMP = 0xFFFF


def ReadTemperatures(startDate, endDate):
    readings = []
    count = 0
    db = settings.DATABASES['default']
    con = psycopg2.connect(database=db['NAME'], user=db['USER'],
                           password=db['PASSWORD'], host=db['HOST'], port=db['PORT'])
    cur = con.cursor()
    sql = "SELECT id, sensor, name, temp, date, guid, remarks FROM TempReadings"
    cur.execute(sql)
    readOk = True
    while readOk:
        data = cur.fetchone()
        if data is None:
            readOk = False
            break

        if data[4] >= endDate and data[4] <= startDate:
            readings[count] = data[3]
            count = count + 1
    return readings


start = datetime.now() - timedelta(days=1)
end = datetime.now()
temps = ReadTemperatures(start, end)
for t in temps:
    print(t)
