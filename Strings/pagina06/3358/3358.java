import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);
        Character[] vogais = {'a', 'e', 'i', 'o', 'u'};
        int n = input.nextInt();

        input.nextLine();

        for (int i = 0; i < n; i++) {
            int count = 0;
            boolean hard = false;
            String sobrenome = input.nextLine();

            for (int j = 0; j < sobrenome.length(); j++) {
                char letra = Character.toLowerCase(sobrenome.charAt(j));

                if (!Arrays.asList(vogais).contains(letra)) {
                    count++;
                } else {
                    count = 0;
                }

                if (count == 3) {
                    hard = true;
                    break;
                }
            }

            if (hard) {
                System.out.println(sobrenome + " nao eh facil");
            } else {
                System.out.println(sobrenome + " eh facil");
            }
        }

        input.close();
    }
}
