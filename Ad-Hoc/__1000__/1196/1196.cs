using System;
using System.Collections.Generics;

class URI {

    static void Main() {
        string teclado = " ` 1234567890-=\nQWERTYUIOP[]\\\nASDFGHJKL;'\nZXCVBNM,./";

        var mapeamento = new Dictionary<char, char>();
        foreach (var linha in teclado.Split('\n')){
            for(int i = 1; i < linha.Length; i++){
                mapeamento[linha[i]] = linha[i - 1];
            }
        }

        string input;
        while((input = Console.ReadLine()) != null){

            string resultado = "";
            foreach(char c in input){
                if(c == " ")
                    resultado += ' ';
                else if(mapeamento.ContainsKey(c))
                    resultado += mapeamento[c];
                else
                    resultado += c;
            }
            Console.WriteLine(resultado);
        }
    }
}