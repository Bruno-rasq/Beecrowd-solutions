using System;
using System.Linq;

public class URI
{
    static void Main()
    {
        int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int h1 = input[0], m1 = input[1], h2 = input[2], m2 = input[3];

        int inicio = h1 * 60 + m1;
        int fim = h2 * 60 + m2;

        int duracao = fim - inicio;
        if (duracao <= 0)
        {
            duracao += 24 * 60; // Adiciona 24h se terminou no dia seguinte ou mesmo horário
        }

        int horas = duracao / 60;
        int minutos = duracao % 60;

        Console.WriteLine($"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)");
    }
}
