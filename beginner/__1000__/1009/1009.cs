using System;
using System.Globalization;

public class URI
{
    public static void Main(string[] args)
    {
        string name = Console.ReadLine();

        double salary = double.Parse(Console.ReadLine());
        double sales = double.Parse(Console.ReadLine());

        double bonus = (sales * 15)/ 100;

        salary += bonus;

        Console.WriteLine("TOTAL = R$ {0}", salary.ToString("F2", CultureInfo.InvariantCulture));
    }
}