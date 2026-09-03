import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        while (in.hasNextLine()) {
            String alien_vowels = in.nextLine();

            if (!in.hasNextLine()) break;

            String frases = in.nextLine();

            int contador = 0;

            for (int i = 0; i < frases.length(); i++) {
                if (alien_vowels.contains(String.valueOf(frases.charAt(i)))) {
                    contador++;
                }
            }

            System.out.println(contador);
        }

        in.close();
    }
}
