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

        String[] entradaStr = input.nextLine().split(" ");
        int[] entrada =new int[entradaStr.length()];
        int count = 0;

        for(int i = 0; i < entradaStr.length; i++){
            entrada[i] = Integer.parseInt(entradaStr[i]);
        }


        entrada[0] = entrada[0] + entrada[1];

        while(entrada[0] >= entrada[2]){
            entrada[0] = (enrada[0] - entrrada[2] + 1);
            count++;
        }

        System.out.println(count);


        input.close();
	}
}