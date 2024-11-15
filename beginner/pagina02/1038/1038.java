import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        double[] prices = {4.00, 4.50, 5.00, 2.00, 1.50};

        int code = in.nextInt();
        int qnt = in.nextInt();

        double valor = prices[code - 1] * qnt;

        System.out.println("Total: R$ " + String.format("%.2f", valor));

        in.close();
    }
}