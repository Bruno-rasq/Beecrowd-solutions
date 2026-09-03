using System;
using System.Globalization;

public class URI
{
    static void Main()
    {
        int line = int.Parse(Console.ReadLine());
        int _qnt = 0;
        double _sum = 0.0;
        double curr = 0.0;
        char OP = Console.ReadLine()[0];
        
        
        for(int i = 0; i < 12; i++){
            if(i > line) break;
            
            for(int j = 0; j < 12; j++){
                curr = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                
                if(i == line){
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