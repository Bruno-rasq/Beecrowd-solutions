using System;

public class URI
{
    public static void Main(string[] args)
    {
        int num_test_cases = int.Parse(Console.ReadLine());

        for (int i = 0; i < num_test_cases; i++)
        {
            Teste_Case();
            if (i < num_test_cases)
                Console.WriteLine();
        }
    }

    public static void Teste_Case()
    {
        int amount_pacs = int.Parse(Console.ReadLine());
        int[,] pacs = new int[amount_pacs, 2];

        for (int i = 0; i < amount_pacs; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            pacs[i, 0] = int.Parse(input[0]); // quantidade brinquedos 
            pacs[i, 1] = int.Parse(input[1]); // peso deles
        }

        int[,] dp = KnapsackProblem(50, pacs);
        int max_toys = dp[pacs.GetLength(0), 50];

        int amountItens;
        int totalWeight;
        amountItensInBackpack(dp, pacs, 50, out amountItens, out totalWeight);

        Console.WriteLine("{0} brinquedos", max_toys);
        Console.WriteLine("Peso: {0} kg", totalWeight);
        Console.WriteLine("sobra(m) {0} pacote(s)", amount_pacs - amountItens);
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

    public static void amountItensInBackpack(
        int[,] dp, int[,] itens, int capacity, out int amountItens, out int totalWeight
    )
    {
        amountItens = 0;
        totalWeight = 0;
        
        int row = itens.GetLength(0);
        int col = capacity;

        while (row > 0 && col > 0)
        {
            if (dp[row, col] != dp[row - 1, col])
            {
                int itemWeight = itens[row - 1, 1];
                col -= itemWeight;
                totalWeight += itemWeight;
                amountItens++;
            }
            row--;
        }
    }
}