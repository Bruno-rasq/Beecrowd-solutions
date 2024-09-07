import java.util.Scanner;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {

		double n;
		Scanner in = new Scanner(System.in);

		n = in.nextDouble();

		for(int i = 0; i<100; i++){
			System.out.printf("N[%d] = %.4f\n", i, n );
			n /= 2.0;
		}

		in.close();
	}
}