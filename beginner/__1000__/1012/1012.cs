using System;
using System.Globalization;

public class URI
{
    public static void Main(string[] args)
    {
        string[] input;
        double a, b, c;

        input = Console.ReadLine().Split(' ');

        a = double.Parse(input[0]);
        b = double.Parse(input[1]);
        c = double.Parse(input[2]);

        LOG("TRIANGULO: ", triangulo(a, c));
        LOG("CIRCULO: ", circle(c));
        LOG("TRAPEZIO: ", trapezio(a, b, c));
        LOG("QUADRADO: ", square(b));
        LOG("RETANGULO: ", retangle(a, b));
    }

    public static void LOG(string message, double value)
    {
        Console.WriteLine("{0}{1}", message, 
            value.ToString("F3", CultureInfo.InvariantCulture));
    }

    public static double triangulo(double a, double c)
    {
        return (a * c) / 2.0;
    }

    public static double circle(double c)
    {
        const double PI = 3.14159;
        return (c * c) * PI;
    }

    public static double trapezio(double a, double b, double c)
    {
        return ((a + b) * c) / 2.0;
    }

    public static double square(double b)
    {
        return b * b;
    }

    public static double retangle(double a, double b)
    {
        return a * b;
    }
}