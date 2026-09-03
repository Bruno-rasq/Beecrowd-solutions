using System;
using System.Globalization;

public class URI 
{
    public static void Main(string[] args)
    {

        double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());
        double c = double.Parse(Console.ReadLine());

        double average = (a * 2 + b * 3 + c * 5) / 10.0;

        Console.WriteLine("MEDIA = {0}", average.ToString("F1", CultureInfo.InvariantCulture));
    }
}
