import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {
    public static void main(String[] args) throws IOException {
        
        DecimalFormat df = new DecimalFormat("#0.000000");
        Scanner input = new Scanner(System.in);

        double a = input.nextDouble();
        double b = input.nextDouble();

        double r = (
            ((1.0 + a / 100) * (1.0 + b / 100)) - 1.0
        ) * 100;

        String formmated = df.format(r);
        System.out.println(formmated);

        input.close();
    }
}