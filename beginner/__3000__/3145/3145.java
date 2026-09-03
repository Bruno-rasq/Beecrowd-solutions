import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int hobbits = in.nextInt() + 2;
        int km = in.nextInt();

        double result = (double) km / hobbits;

        System.out.println(String.format("%.2f", result));
    }
}