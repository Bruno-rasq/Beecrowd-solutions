using System;
using System.Globalization;

class Program {
    static void Main(string[] args) {
        
        string[] input = Console.ReadLine().Trim().Split(' ');

        double a = double.Parse(input[0]);
        double b = double.Parse(input[1]);
        double c = double.Parse(input[2]);

        double resultado = (a * b * c) / (a * b + a * c + b * c);

        Console.WriteLine(resultado.ToString("F3", CultureInfo.InvariantCulture));
    }
}