import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);

		int a = Integer.parseInt(in.readLine());
		int b = Integer.parseInt(in.readLine());

		System.out.printf("SOMA = %d\n", (a + b));
	}
}