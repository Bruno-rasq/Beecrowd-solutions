import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		
		String[] linha1 = in.readLine().trim().split(" ");
		int quantidade1 = Integer.parseInt(linha1[1]);
		double valor1 = Double.parseDouble(linha1[2]);
		
		String[] linha2 = in.readLine().trim().split(" ");
		int quantidade2 = Integer.parseInt(linha2[1]);
		double valor2 = Double.parseDouble(linha2[2]);

		System.out.printf("VALOR A PAGAR: R$ %.2f\n", (quantidade1 * valor1) + (quantidade2 * valor2));
	}
}