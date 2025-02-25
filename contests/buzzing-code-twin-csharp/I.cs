using System;

class URI {
    static void Main() {
        int n = int.Parse(Console.ReadLine());
        string[] words = Console.ReadLine().Split(' ');

        string correctWords = '';
        for(int i = 0; i < n; i++){
            string word = words[i];

            if(!string.IsNullOrEmpty(correctWords))
                correctWords += " ";
            
            if(word.Length == 3){
                if(word.StartWith("OB")){
                    correctWords += "OBI";
                    continue;
                }
                if(word.StartWith("UR")){
                    correctWords += "URI";
                    continue;
                }
            }
            correctWords += word;
        }
        Console.WriteLine(correctWords);
    }
}