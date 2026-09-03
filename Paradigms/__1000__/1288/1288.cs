using System;

public class URI
{
    public static void Main(string[] args)
    {
        int numberTests = int.Parse(Console.ReadLine());
        for (int i = 0; i < numberTests; i++)
        {
            Teste_Case();
        }
    }

    public static void Teste_Case()
    {
        int nLeadPieces = int.Parse(Console.ReadLine());
        int[,] leadPieces = new int[nLeadPieces, 2];

        // ✅ Adicionadas chaves ao for
        for (int i = 0; i < nLeadPieces; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            int damage = int.Parse(input[0]);
            int weight = int.Parse(input[1]);

            // ✅ Forma correta de preencher o array 2D
            leadPieces[i, 0] = damage;
            leadPieces[i, 1] = weight;
        }

        int loadCapacity = int.Parse(Console.ReadLine());
        int castleHP = int.Parse(Console.ReadLine());

        int[,] dp = KnapsackProblem(loadCapacity, leadPieces);
        int maxDamage = dp[leadPieces.GetLength(0), loadCapacity];

        Console.WriteLine(
            maxDamage >= castleHP
                ? "Missao completada com sucesso"
                : "Falha na missao"
        );
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