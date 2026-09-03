import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] agrs) throws IOException {

        Scanner input = new Scanner(System.in);

        double[] data = new double[4];

        data[0] = input.nextDouble();
        data[1] = input.nextDouble();
        data[2] = input.nextDouble();
        data[3] = input.nextDouble();

        double distance = Math.sqrt(
            Math.pow((data[2] - data[0]), 2) + Math.pow((data[1] - data[3]), 2)
        );

        System.out.println(String.format("%.4f", distance));

    }
}