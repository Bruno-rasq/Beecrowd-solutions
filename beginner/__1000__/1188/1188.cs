using System;
using System.Globalization;

public class URI 
{
    static void Main()
    {
        char OPERATION = Console.ReadLine()[0];
        double sum = 0;
        int counter = 0;
        int interval_I = 5;
        int interval_F = 6;
        
        // descartar a metade superior (6 linhas × 12 colunas)
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 12; j++)
            {
                Console.ReadLine();
            } 
        }
        
        // processar a metade inferior (6 linhas restantes)
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 12; j++)
            { 
                double curr = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                if (j > interval_I && j < interval_F)
                {
                    sum += curr;
                    counter++;
                }
            }
            interval_I--;   // intervalo "abre" para a esquerda
            interval_F++;   // intervalo "abre" para a direita
        }
        
        double average = sum / counter;
        double response = OPERATION == 'M' ? average : sum;
    
        Console.WriteLine(response.ToString("F1", CultureInfo.InvariantCulture));
    }
}