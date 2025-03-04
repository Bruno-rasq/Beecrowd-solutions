import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int intTestCases = Integer.parseInt(scanner.nextLine()); // Lê o número de casos de teste

        for (int i = 0; i < intTestCases; i++) {
            String line = scanner.nextLine();
            String[] data = line.split(""); // Converte a linha em um array de caracteres

            // Filtra apenas os caracteres '<' e '>'
            StringBuilder filteredData = new StringBuilder();
            for (String ch : data) {
                if (ch.equals("<") || ch.equals(">")) {
                    filteredData.append(ch);
                }
            }

            int diamonds = 0;
            int openCount = 0;

            // Processa os caracteres filtrados
            for (int j = 0; j < filteredData.length(); j++) {
                if (filteredData.charAt(j) == '<') {
                    openCount++; // Aumenta a contagem de aberturas
                } else if (filteredData.charAt(j) == '>') {
                    if (openCount > 0) {
                        openCount--; // Fecha uma abertura
                        diamonds++;  // Conta um diamante
                    }
                }
            }

            System.out.println(diamonds); // Imprime o número de diamantes
        }

        scanner.close();
    }
}