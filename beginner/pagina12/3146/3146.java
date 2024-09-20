import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws IOException {
		
        Scanner input = new Scanner(System.in);

        double r = input.nectDouble();
        double PI= 3.14;
        double circunferencia = 2 * ( PI * r);

        System.out.println(String.format("%.2f", circunferencia));

        input.close();
	}
}