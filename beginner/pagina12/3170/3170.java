import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws IOException {
		
        Scanner input = new Scanner(System.in);

        int b = input.nextInt();
        int g = input.nextInt();

        int result = (g / 2) - b;

        if(result <= 0){
            System.out.println("Amelia tem todas bolinhas!");
        } else {
            System.out.println("Faltam " + result + " bolinha(s)!");
        }

        input.close();
	}
}