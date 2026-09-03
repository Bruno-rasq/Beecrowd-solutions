import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir); 

		String vendedor = in.readLine();		
		double salary = Double.parseDouble(in.readLine());
		double sales = Double.parseDouble(in.readLine());

		double bonus = (sales * 15) / 100.0;

		System.out.printf("TOTAL = R$ %.2f\n", salary + bonus);
	}
}