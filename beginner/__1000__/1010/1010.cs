using System;
using System.Globalization;

public class URI
{
    public static void Main(string[] args)
    {
        string[] line1, line2;
        int code1, qnt1, code2, qnt2;
        double price1, price2, total;

        line1 = Console.ReadLine().Split(' ');
        line2 = Console.ReadLine().Split(' ');

        code1   = int.Parse(line1[0]);
        qnt1    = int.Parse(line1[1]);
        price1  = double.Parse(line1[2]);

        code2   = int.Parse(line2[0]);
        qnt2    = int.Parse(line2[1]);
        price2  = double.Parse(line2[2]);

        total = (price1 * qnt1) + (price2 * qnt2);

        Console.WriteLine("VALOR A PAGAR: R$ {0}", 
            total.ToString("F2", CultureInfo.InvariantCulture));
    }
}