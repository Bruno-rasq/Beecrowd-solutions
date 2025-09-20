using System;
using System.Globalization;

public class URI {
    static void Main(){
        char OPERADOR = Console.ReadLine()[0];
        int counter = 0;
        float sum = 0.0f;

        float[,] matrix = new float[12, 12];
        for(int i = 0; i < 12; i++ ){
            for(int j = 0; j < 12; j++){
                matrix[i,j] = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            }
        } 

        int k = 11;
        for(int i = 0; i < 12; i++){
            for(int j = 0; j < 12; j++){
                if(j > k){
                    sum += matrix[i, j];
                    counter++;
                }
            }
            k--;
        }

        if(OPERADOR == 'M'){
            float average = sum / counter;
            Console.lWriteLine(average.ToString("F1", CultureInfo.InvariantCulture));
            return;
        }
        Console.lWriteLine(sum.ToString("F1", CultureInfo.InvariantCulture));
    }
}