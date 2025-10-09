using System;

public class URI
{
    public static void Main()
    {
        int a, b, c, d;

        a = int.Parse(Console.ReadLine());
        b = int.Parse(Console.ReadLine());
        c = int.Parse(Console.ReadLine());
        d = int.Parse(Console.ReadLine());

        int diff = (a * b) - (c * d);

        Console.WriteLine("DIFERENCA = {0}", diff);
    }
}