import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir); 

		double a = Double.parseDouble(in.readLine());
		double b = Double.parseDouble(in.readLine());
		double average = ((a * 3.5) + (b * 7.5)) / 11;

		System.out.printf("MEDIA = %.5f\n", average);
	}
}