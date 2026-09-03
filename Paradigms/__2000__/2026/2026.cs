using System;

public class URI
{
    public static void Main(string[] args)
    {
        int num_test_cases = int.Parse(Console.ReadLine());

        for (int i = 0; i < num_test_cases; i++)
        {
            Teste_Case(i + 1);
            if (i < num_test_cases)
                Console.WriteLine();
        }
    }

    public static void Teste_Case(int num_test)
    {
        int amount_packages = int.Parse(Console.ReadLine());
        int capacity = int.Parse(Console.ReadLine());
        int[,] pacs = new int[amount_packages, 2];

        for (int i = 0; i < amount_packages; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            pacs[i, 0] = int.Parse(input[0]); // qnt de ornamentos por pacote
            pacs[i, 1] = int.Parse(input[1]); // peso do pacote
        }

        int[,] dp = KnapsackProblem(capacity, pacs);
        int max_ornaments = dp[pacs.GetLength(0), capacity];

        Console.WriteLine("Galho {0}:", num_test);
        Console.WriteLine("Numero total de enfeites: {0}", max_ornaments);
    }

    public static int[,] KnapsackProblem(int capacity, int[,] itens)
    {
        int numItens = itens.GetLength(0);
        int[,] dp = new int[numItens + 1, capacity + 1];

        for (int i = 1; i <= numItens; i++)
        {
            int currentItemValue = itens[i - 1, 0];
            int currentItemWeight = itens[i - 1, 1];

            for (int j = 0; j <= capacity; j++)
            {
                if (j < currentItemWeight) 
                    dp[i, j] = dp[i - 1, j];
                else
                {
                    int remainingCapacity = j - currentItemWeight;
                    int addedValue = dp[i - 1, remainingCapacity] + currentItemValue;
                    dp[i, j] = Math.Max(dp[i - 1, j], addedValue);
                }
            }
        }

        return dp;
    }
    
}