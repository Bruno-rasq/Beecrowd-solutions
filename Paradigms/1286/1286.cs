using System;

public class URI
{
    public static void Main(string[] args)
    {
        while(true)
        {
            int num_deliveries = int.Parse(Console.ReadLine());
            if (num_deliveries == 0) break;
            
            Teste_Case(num_deliveries);
        }
    }

    public static void Teste_Case(int num_deliveries)
    {
        int max_pizza_delivered = int.Parse(Console.ReadLine());
        int[,] deliveries = new int[num_deliveries, 2];

        for (int i = 0; i < num_deliveries; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            deliveries[i, 0] = int.Parse(input[0]); // tempo em min
            deliveries[i, 1] = int.Parse(input[1]); // qnt pizza
        }

        int[,] dp = KnapsackProblem(max_pizza_delivered, deliveries);
        int max_time = dp[deliveries.GetLength(0), max_pizza_delivered];

        Console.WriteLine("{0} min.", max_time);
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
                {
                    dp[i, j] = dp[i - 1, j];
                }
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