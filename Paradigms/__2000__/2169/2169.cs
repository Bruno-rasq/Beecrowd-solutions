using System;
using System.Collections.Generic;

public class URI
{
    public const string SUCESS = "Missao completada com sucesso";
    public const string FAIL = "You Are Dead";

    // Tabela de armas (dano por munição)
    static readonly Dictionary<string, double> WEAPONS = new Dictionary<string, double>
    {
        {"HANDGUN", 2.0}, {"RED9", 3.5},
        {"BLACKTAIL", 3.5}, {"MATILDA", 2.0},
        {"HANDCANNON", 60.0}, {"STRIKER", 12.0},
        {"TMP", 1.2}, {"RIFLE", 12.0}
    };

    // Tabela de inimigos e HP
    static readonly Dictionary<string, int> ENEMIES = new Dictionary<string, int>
    {
        {"GANADOS", 50}, {"COBRAS", 40}, {"ZEALOT", 75},
        {"COLMILLOS", 60}, {"GARRADOR", 125}, {"LASPLAGAS", 100},
        {"GATLINGMAN", 150}, {"REGENERATOR", 250},
        {"ELGIGANTE", 500}, {"DR.SALVADOR", 350}
    };

    // Estrutura equivalente ao vector<tuple<double,int>>
    public struct Item
    {
        public double Damage;
        public int Ammo;
        public Item(double damage, int ammo)
        {
            Damage = damage;
            Ammo = ammo;
        }
    }

    public static int[,] KnapsackProblem(List<Item> itens, int capacity)
    {
        int rows = itens.Count + 1;
        int cols = capacity + 1;
        int[,] dp = new int[rows, cols];

        for (int i = 1; i < rows; i++)
        {
            double currDamage = itens[i - 1].Damage;
            int currAmmo = itens[i - 1].Ammo;

            for (int j = 0; j < cols; j++)
            {
                if (j < currAmmo)
                {
                    dp[i, j] = dp[i - 1, j];
                }
                else
                {
                    int remaining = j - currAmmo;
                    int addedValue = dp[i - 1, remaining] + (int)currDamage;
                    dp[i, j] = Math.Max(dp[i - 1, j], addedValue);
                }
            }
        }

        return dp;
    }

    public static void Main(string[] args)
    {
        string input;
        while ((input = Console.ReadLine()) != null)
        {
            int nWeapons = int.Parse(input);
            var weapons = new List<Item>();

            // leitura das armas
            for (int i = 0; i < nWeapons; i++)
            {
                string[] parts = Console.ReadLine().Split(' ');
                string weaponName = parts[0];
                int ammo = int.Parse(parts[1]);
                double damage = WEAPONS[weaponName] * ammo;

                weapons.Add(new Item(damage, ammo));
            }

            // leitura dos inimigos
            int nEnemies = int.Parse(Console.ReadLine());
            int totalEnemiesHP = 0;
            for (int i = 0; i < nEnemies; i++)
            {
                string[] parts = Console.ReadLine().Split(' ');
                string enemyName = parts[0];
                int amount = int.Parse(parts[1]);
                totalEnemiesHP += ENEMIES[enemyName] * amount;
            }

            // capacidade da mochila
            int capacity = int.Parse(Console.ReadLine());
            int[,] dp = KnapsackProblem(weapons, capacity);
            double maxDamage = dp[nWeapons, capacity];

            Console.WriteLine(totalEnemiesHP - maxDamage <= 0 ? SUCESS : FAIL);
            Console.WriteLine();
        }
    }
}