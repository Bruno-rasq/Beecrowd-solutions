using System;
using System.Collections.Generic;

public class URI
{
    // Lista de deltas do cavalo (dx, dy)
    private static readonly (int dx, int dy)[] deltas =
    {
        ( 2,  1), ( 1,  2), (-1,  2), (-2,  1),
        (-2, -1), (-1, -2), ( 1, -2), ( 2, -1)
    };

    public static void Main(string[] args)
    {
        string line;
        while ((line = Console.ReadLine()) != null && line != "")
        {
            var input = line.Split(' ');
            var source = GetCoord(input[0]);
            var target = GetCoord(input[1]);

            int moves = BFS(source, target);

            Console.WriteLine(
                $"To get from {input[0]} to {input[1]} takes {moves} knight moves."
            );
        }
    }

    // Transforma a posição (ex: "a1") em coordenadas (linha, coluna)
    public static (int x, int y) GetCoord(string position)
    {
        int col = position[0] - 'a'; // a→0, b→1, ...
        int row = position[1] - '1'; // 1→0, 2→1, ...
        return (row, col);
    }

    // BFS para calcular menor número de movimentos do cavalo
    public static int BFS((int x, int y) source, (int x, int y) target)
    {
        var queue = new Queue<(int moves, int x, int y)>();
        var visited = new HashSet<(int x, int y)>();

        queue.Enqueue((0, source.x, source.y));
        visited.Add(source);

        while (queue.Count > 0)
        {
            var (moves, x, y) = queue.Dequeue();

            if (x == target.x && y == target.y)
                return moves;

            for (int i = 0; i < deltas.Length; i++)
            {
                int nx = x + deltas[i].dx;
                int ny = y + deltas[i].dy;

                if (InBound(nx, ny) && !visited.Contains((nx, ny)))
                {
                    visited.Add((nx, ny));
                    queue.Enqueue((moves + 1, nx, ny));
                }
            }
        }

        return -1; // Nunca deve acontecer no tabuleiro 8x8
    }

    // Verifica se está dentro dos limites do tabuleiro 8x8
    public static bool InBound(int x, int y)
    {
        return (0 <= x && x < 8 && 0 <= y && y < 8);
    }
}