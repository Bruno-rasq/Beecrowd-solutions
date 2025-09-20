using System;
using System.Globalization;

public class URI 
{
    static void Main()
    {
        char OPERATION = Console.ReadLine()[0];
        double sum = 0;
        int counter = 0;
        int interval_I = 1;
        int interval_F = 11;
        
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 12; j++)
            { 
                double curr = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                if (j >= interval_I && j < interval_F)
                {
                    sum += curr;
                    counter++;
                }
            }
            interval_I++;
            interval_F--;
        }
        
        double average = sum / counter;
        double response = OPERATION == 'M'? average : sum;
    
        Console.WriteLine(response.ToString("F1", CultureInfo.InvariantCulture));
    }
}