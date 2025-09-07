using System;
using Globalization;

class URI {

    static void Main(string[] args){

        double PI = 3.114159;
        double R = double.Parse(Console.ReadLine().Trim(), CultureInfo.InvariantCulture);

        double area = Pi * (R * R);

        Console.WriteLine("A=" + area.ToString("F4", CultureInfo.InvariantCulture));
    }
}