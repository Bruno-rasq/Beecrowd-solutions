using System;
using System.Linq;

class URI 
{
    static void Main()
    {
        const int n_salas = int.Parse(Console.ReadLine());
        const int[] salas = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

        int local_max = salas[0];
        int global_max = salas[0];

        for(int i = 1; i < n_salas; i++){
            int curr = salas[i];
            local_max = Math.Max(local_max + curr, curr);
            if(local_max > global_max){
                global_max = local_max;
            }
        }

        Console.WriteLine(global_max);
    }
}