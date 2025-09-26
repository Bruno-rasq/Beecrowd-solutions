using System;
using System.Globalization;

public class URI
{
    static void Main()
    {
        char OP = Console.ReadLine()[0];
        double _sum = 0.0;
        int _qnt = 0;
        
        
        for(int i = 0; i < 12; i++){
            for(int j = 0; j < 12; j++){
                
                double curr = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                bool conditiontop = (i < 6 && j < i);
                bool conditionbottom = (i > 5 && j < 11 - i);
                
                if(conditiontop || conditionbottom){
                    _sum += curr;
                    _qnt += 1;
                }
            }
        }
        
        double average = _sum / _qnt;
        double response = OP == 'M' ? average : _sum;
        
        Console.WriteLine(response.ToString("F1", CultureInfo.InvariantCulture));
    }
}