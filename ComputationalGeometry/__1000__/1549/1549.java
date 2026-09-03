import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int pessoas = sc.nextInt();
            int mililitros = sc.nextInt();
            int b = sc.nextInt();
            int B = sc.nextInt();
            int H = sc.nextInt();

            double media = (double) mililitros / pessoas;
            double temp = Math.cbrt((media * 3 * (B - b) / (Math.PI * H)) + Math.pow(b, 3));
            double h = media * 3 / (Math.PI * (Math.pow(temp, 2) + temp * b + Math.pow(b, 2)));

            System.out.printf("%.2f%n", h);
        }

        sc.close();
    }
}