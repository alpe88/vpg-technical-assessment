using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;

namespace TestTemp
{
    
    internal class Program
    {
        private static string dataConnectionString = "Data Source=tcp:xxx.database.windows.net;Initial Catalog=mydb;Integrated Security=False;Persist Security Info=False;User ID=xxx;Password=xxxxxx;";
        private static int MAX_TEMP = 0xFFFF;

        static List<int> ReadTemperatures(DateTime startDate, DateTime endDate)
        {
            int[] temps = new int[MAX_TEMP];
            int count = 0;
            SqlConnection connection = new SqlConnection(dataConnectionString);
            SqlCommand command = new SqlCommand("SELECT id, sensor, name, temp, date, guid, remarks FROM TempReadings", connection);
            SqlDataReader set = command.ExecuteReader();
            bool readOk = true; 
            while (readOk == true)
            {
                readOk = set.Read();
                DateTime date = (DateTime)set["date"];
                if (date >= startDate && date <= endDate)
                    temps[count] = int.Parse(set["temp"].ToString());
                count++;
            }
            return temps.ToList();
        }

        static void Main(string[] args)
        {
            List<int> temps = ReadTemperatures(DateTime.Now.AddDays(-1), DateTime.Now);
            for (int i = 0; i< temps.Count; i++)
                Console.WriteLine(temps[i]);
        }
    }
}
