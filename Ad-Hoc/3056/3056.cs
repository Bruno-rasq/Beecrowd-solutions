using System;

public class URI {
    static void Main(string[] args) {
        
        int steps = int.Parse(Console.ReadLine().Trim());
        long nodes = 2;
        
        for(int i = 0; i < steps; i++){
            nodes += (nodes - 1);
        }
        
        Console.WriteLine(nodes * nodes);
    }
}