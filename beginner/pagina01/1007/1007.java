import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir); 

		ArrayList<Integer> list = new ArrayList();
		for(int i = 0; i < 4; i++){
			list.add(Integer.parseInt(in.readLine()));
		}

		int diference = (list.get(0) * list.get(1)) - (list.get(2) * list.get(3));
	
		System.out.printf("DIFERENCA = %d\n", diference);
	}
}