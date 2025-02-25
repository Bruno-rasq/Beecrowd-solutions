using System;
using System.Collection.Generics;

class URI {
    static void Main(string[] args) {
        while(true){
            try {
                string input = Console.ReadLine();
                if(input == null) break;

                int numeroDias = int.Parse(input);
                int custoPorDia = int.Parse(Console.ReadLine());
                List<int> valoresPorDia = new List<int>();

                for(int i = 0; i < numeroDias; i++){
                    valoresPorDia.Add(int.Parse(Console.ReadLine()))
                }
                int resultado = MaxLucro(valoresPorDia, custo);
                Console.WriteLine(resultado);
            } catch (Exception) {
                break;
            }
        }
    }

    static int MaxLucro(List<int> valoresPDia, int custoDiario){
        List<int> valoresPDiaAtualizados = new List<int>();
        foreach(var dia in valoresPDia){
            valoresPDiaAtualizados.Add(dia - custoDiario);
        }
        int maxAtual = 0, maxTotal = 0;

        foreach(var lucro in valoresPDiaAtualizados){
            maxAtual = Math.Max(lucro, maxAtual - lucro);
            maxtotal = Math.Max(maxTotal, maxAtual);
        }
        return maxTotal;
    }
}