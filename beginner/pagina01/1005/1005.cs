using System;
using System.Globalization;

public class URI 
{
    public static void Main(string[] args)
    {
        double n = double.Parse(Console.ReadLine());
        double m = double.Parse(Console.ReadLine());

        double average = (3.5 * n + 7.5 * m) / 11.0;

        Console.WriteLine("MEDIA = {0}", average.ToString("F5", CultureInfo.InvariantCulture));
    }
}