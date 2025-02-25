using System;

class URI {
    static int calls = 0;

    static int Fib(int n){
        if(n == 1 || n == 0)
            return n;

        calls += 2;
        return fib(n - 1) + Fib(n - 2);
    }

    static void Main(string[] args){
        int n = int.Parse(Console.ReadLine());
        for(int i = 0; i < n; i++){
            int input = int.Parse(Console.ReadLine());
            calls = 0;

            int output = Fib(input);

            Console.WriteLine($"fib({input}) = {calls} calls = {output}");
        }
    }
}