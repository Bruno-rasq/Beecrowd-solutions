using System;
using System.Linq;

public class URI 
{
    static void get_input(ref int[] input)
    {
        input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    }
    
    static (int, int) get_adj_coord(int[,] grid, int x, int y)
    {
        var deltaMove = new (int, int)[]{(0, 1), (0, -1), (1, 0), (-1, 0)};
        
        foreach (var move in deltaMove)
        {
            int dx = move.Item1;
            int dy = move.Item2;
    
            int nx = dx + x;
            int ny = dy + y;
    
            bool in_bound = nx >= 0 && nx < grid.GetLength(0) && ny >= 0 && ny < grid.GetLength(1);
            if (in_bound && grid[nx, ny] == 1)
                return (nx, ny);
        }
        return (-1, -1);
    }
    
    static (int, int) get_final_coord(int[,] grid, int x, int y)
    {
        grid[x, y] = 0;
        while (true)
        {
            var (nx, ny) = get_adj_coord(grid, x, y);
            if (nx == -1) break;
            x = nx;
            y = ny;
            grid[x, y] = 0;
        }
        return (x + 1, y + 1);
    }
    
    static void Main()
    {
        int[] input = null;
        
        get_input(ref input);
        (int n, int m) = (input[0], input[1]);
        
        get_input(ref input);
        (int x, int y) = (input[0] - 1, input[1] - 1);
        
        int[,] grid = new int[n, m];
        for (int i = 0; i < n; i++)
        {
            get_input(ref input);
            for (int j = 0; j < m; j++) 
                grid[i, j] = input[j];
        }
        
        (int coordx, int coordy) = get_final_coord(grid, x, y);
        Console.WriteLine($"{coordx} {coordy}");
    }
}