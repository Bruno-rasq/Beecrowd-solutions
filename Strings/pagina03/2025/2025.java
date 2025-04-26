import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int n = Integer.parseInt(input.nextLine());

        for (int i = 0; i < n; i++) {
            String[] mensagem = input.nextLine().split(" ");
            String[] corrigida = new String[mensagem.length];

            for (int j = 0; j < mensagem.length; j++) {
                String palavra = mensagem[j];
                corrigida[j] = corrigirPalavra(palavra);
            }

            System.out.println(String.join(" ", corrigida));
        }

        input.close();
    }

    public static String corrigirPalavra(String palavra) {
        if (palavra.length() == 10 && palavra.substring(1, 9).equals("oulupukk")) {
            return "Joulupukki";
        } else if (palavra.length() == 11 && palavra.substring(1, 9).equals("oulupukk") && palavra.endsWith(".")) {
            return "Joulupukki.";
        }
        return palavra;
    }
}
