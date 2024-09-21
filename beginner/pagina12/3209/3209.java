import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        input.nextLine();

        for(int i = 0; i < n; i++){
            
            String[] data = input.nextLine().split(" ");

            int reguas = Integer.parseInt(data[0]);
            int total = Integer.parseInt(data[1]);

            for(int j = 2; j < reguas + 1; j++){
                int curr = Integer.parseInt(data[j]);
                total = (total - 1) + curr;
            }

            System.out.println(total);
        }
	}
}