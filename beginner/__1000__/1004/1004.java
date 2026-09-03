import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir); 

		int a = Integer.parseInt(in.readLine());
		int b = Integer.parseInt(in.readLine());
		int prod = a * b;

		System.out.printf("PROD = %d\n", prod);
	}
}