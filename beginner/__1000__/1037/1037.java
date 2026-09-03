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
		// code

        Scanner input = new Scanner(System.in);

        double Num = input.nextDouble();

        if(Num < 0 ){
            System.out.println("Fora de intervalo");

        } else if ( Num >= 0 && Num <= 25 ){
            System.out.println("Intervalo [0,25]");

        } else if ( Num >= 25 && Num <= 50 ){
            System.out.println("Intervalo (25,50]");

        } else if( Num >= 50 && Num <= 75 ){
            System.out.println("Intervalo (50,75]");

        } else if ( Num >= 75 && Num <= 100 ){
            System.out.println("Intervalo (75,100]");

        } else if ( Num > 100 ){
            System.out.println("Fora de intervalo");
        }
	}
}