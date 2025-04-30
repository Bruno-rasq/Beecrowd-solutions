import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int i = 1;
        String palavra = input.nextLine();
        while (!palavra.equals("*")) {
            wordPlay(palavra, i);
            i++;
            palavra = input.nextLine();
        }

        input.close();
    }

    public static void wordPlay(String palavra, int i){
        String menor = palavra;
        String maior = palavra;
        String dupla = palavra + palavra;

        for (int j = 1; j < palavra.length(); j++) {
            String rotacionada = dupla.substring(j, j + palavra.length());
            if (rotacionada.compareTo(menor) < 0) {
                menor = rotacionada;
            }
            if (rotacionada.compareTo(maior) > 0) {
                maior = rotacionada;
            }
        }

        System.out.println("Caso " + i + ": " + menor + " " + maior);
    }
}
