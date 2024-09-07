import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);

        double r = input.nextDouble();
        double pi = 3.14159;

        double volume = (r * r * r) * pi * (4.0/3.0);

        System.out.println(String.format("VOLUME = %.3f", volume));

        input.close();
    }
}