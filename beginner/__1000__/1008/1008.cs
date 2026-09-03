using System;
using System.Globalization;

public class URI
{
    public static void Main(string[] args)
    {
        Console.WriteLine("NUMBER = {0}", Console.ReadLine());

        int worked_hours;
        double receive_per_hour, salary;

        worked_hours = int.Parse(Console.ReadLine());
        receive_per_hour = double.Parse(Console.ReadLine());

        salary = receive_per_hour * worked_hours;

        Console.WriteLine("SALARY = U$ {0}", 
            salary.ToString("F2", CultureInfo.InvariantCulture));
    }
}