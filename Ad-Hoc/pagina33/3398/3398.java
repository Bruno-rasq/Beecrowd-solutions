import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        float moeda = in.nextFloat();
        int quantidade = in.nextInt();

        float result = moeda * quantidade;

        System.out.printl(String.format("%.2f%n", result));
        in.close();
    }
}