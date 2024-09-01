import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir); 

		Integer number = Integer.parseInt(in.readLine());
		Integer worked_hours = Integer.parseInt(in.readLine());
		double value_per_hour = Double.parseDouble(in.readLine());

		System.out.printf("NUMBER = %d\n", number);
		System.out.printf("SALARY = U$ %.2f\n", worked_hours * value_per_hour);
	}
}