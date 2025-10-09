using System;
using System.Globalization;

public class URI
{
    public static double sphereVolume(double raio)
    {
        const double PI = 3.14159;
	    return (4.0 / 3.0) * PI * (raio * raio * raio);
    }

    public static void Main(string[] args)
    {
        double raio = double.Parse(Console.ReadLine());
        double volume = sphereVolume(raio);

        Console.WriteLine("VOLUME = {0}", volume.ToString("F3", CultureInfo.InvariantCulture));
    }
}
