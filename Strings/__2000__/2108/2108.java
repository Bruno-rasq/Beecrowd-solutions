import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);

        int maior = 0;
        String maior_palavra = "";
        String line = in.nextLine();

        while(!line.equals("0")){

            String resultado = "";
            String[] words = line.split(' ');

            for(int i = 0; i < words.length; i++){
                if(!resultado.isEmpty()){ resultado += "-"; }

                if (words[i].length() >= maior){
                    maior = words[i].length();
                    maior_palavra = words[i];
                }

                resultado += words[i].length();
            }

            System.out.println(resultado);
            line = in.nextLine();
        }
        System.out.println("");
        System.out.println("The biggest word: " + maior_palavra);
        in.close();
    }
}