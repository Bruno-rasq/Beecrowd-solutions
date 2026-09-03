import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);

        String john = input.nextLine();
        String medico = input.nextLine();

        if(john.length() >= medico.length()){
            System.out.println("go");

        } else {
            System.out.println("no");

        }
        
        input.close();
	}
}