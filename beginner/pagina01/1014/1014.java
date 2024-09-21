import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void maio(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        int x = input.nextInt();
        double y = input.nextDouble();

        double average = x / y;

        System.out.println(String.format("%.3f", average) + " km/l");
    }
}