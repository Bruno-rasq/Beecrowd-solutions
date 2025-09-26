using System;
using System.Globalization;

public class URI 
{
    static void Main()
    {
        int column = int.Parse(Console.ReadLine());
        int _qnt = 0;
        double _sum = 0.0;
        double curr = 0.0;
        char OP = Console.ReadLine()[0];

        for(int i = 0; i < 12; i++){
            for(int j = 0; j < 12; j++){
                curr = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                if(j == column){
                    _sum += curr;
                    _qnt += 1;
                }
            }
        }

        double average = _sum / _qnt;
        double output = OP == 'M' ? average : _sum;

        Console.WriteLine(output.ToString("F1", CultureInfo.InvariantCulture));
    }
}