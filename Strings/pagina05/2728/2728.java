import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String cobol = "cobol";

        while (in.hasNextLine()) {
            String[] palavras = in.nextLine().split("-");
            boolean valido = true;

            for (int i = 0; i < 5; i++) {
                String curr = palavras[i].toLowerCase();
                String letra = String.valueOf(cobol.charAt(i));

                if (!curr.startsWith(letra) && !curr.endsWith(letra)) {
                    valido = false;
                    break;
                }
            }

            System.out.println(valido ? "GRACE HOPPER" : "BUG");
        }

        in.close();
    }
}
