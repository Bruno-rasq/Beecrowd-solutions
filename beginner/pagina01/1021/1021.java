import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] notas = {10000, 5000, 2000, 1000, 500, 200};
        int[] moedas = {100, 50, 25, 10, 5, 1};
        Scanner scanner = new Scanner(System.in);
        
        String input = scanner.nextLine();
        String[] parts = input.split("\\.");
        int reais = Integer.parseInt(parts[0]) * 100 + Integer.parseInt(parts[1]);

        System.out.println("NOTAS:");
        for (int i = 0; i < 6; ++i) {
            System.out.printf("%d nota(s) de R$ %.2f%n", reais / notas[i], notas[i] / 100.0);
            reais %= notas[i];
        }

        System.out.println("MOEDAS:");
        for (int i = 0; i < 6; ++i) {
            System.out.printf("%d moeda(s) de R$ %.2f%n", reais / moedas[i], moedas[i] / 100.0);
            reais %= moedas[i];
        }
        
        scanner.close();
    }
}
