import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            sc.nextLine(); // consumir a quebra de linha após o número

            int validos = 0;

            for (int i = 0; i < n; i++) {
                String especie = sc.nextLine();
                String raca = sc.nextLine();
                String nome = sc.nextLine();
                sc.nextLine(); // linha vazia

                if (!especie.equals("cachorro")) continue;

                String[] partesNome = nome.trim().split("\\s+");
                if (partesNome.length < 2) continue;

                char inicialRaca = Character.toLowerCase(raca.charAt(0));
                boolean temInicialIgual = false;

                for (String parte : partesNome) {
                    if (Character.toLowerCase(parte.charAt(0)) == inicialRaca) {
                        temInicialIgual = true;
                        break;
                    }
                }

                if (temInicialIgual) validos++;
            }

            System.out.println(validos);
        }

        sc.close();
    }
}