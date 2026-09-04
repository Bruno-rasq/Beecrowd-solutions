using System;

class URI
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split(' ');

        int x1 = int.Parse(input[0]);
        int y1 = int.Parse(input[1]);
        int x2 = int.Parse(input[2]);
        int y2 = int.Parse(input[3]);

        int distanceManhattan = Math.Abs(x1 - x2) + Math.Abs(y1 - y2);

        Console.WriteLine(distanceManhattan);
    }
}
