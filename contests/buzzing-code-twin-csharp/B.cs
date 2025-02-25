using System;
using System.Collection.Generics;

class URI {
    static void Main() {
        List<string> listaAmigosAtual = new List<string>(Console.ReadLine().Split());
        List<string> listaAmigosNova  = new List<string>(Console.ReadLine().Split());
        List<string> listaAtualizada  = new List<string>();
        string amigoIndicado = Console.ReadLine();

        if(amigoIndicado != 'nao' && listaAmigosAtual.Contains(amigoIndicado)){
            foreach(string amigo in listaAmigosAtual){
                if(amigo == amigoIndicado){
                    listaAtualizada.AddRange(listaAmigosNova);
                }
                listaAtualizada.Add(amigo);
            }
        } else {
            listaAtualizada.AddRange(listaAmigosAtual);
            listaAtualizada.AddRange(listaAmigosNova);
        }

        Console.WriteLine(string.Join(' ', listaAtualizada));
    }
}