using System;
using System.Collection.Generics;

class URI {
    static int ArrayHash(List<string> lista){
        int hash = 0;
        for(int i = 0; i < lista.Count; i++){
            string line = lista[i];
            for(int j = 0; j < line.Length; j++){
                int posAfl = line[j] - 'A';
                hash += posAfl + i + j;
            }
        }
        return hash;
    }

    static void Main(){

        int n = int.Parse(Console.ReadLine());
        for(int i = 0; i < n; i++){
            int numeroCasos = int.Parse(Console.ReadLine());
            List<string> words = new List<string>();

            for(int j = 0; j < numeroCasos; j++){
                words.Add(Console.ReadLine());
            }
            Console.WriteLine(ArrayHash(words));
        }
    }
}