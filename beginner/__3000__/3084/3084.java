import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws IOException {

		Scanner input = new Canner(System.in);

        while(input.hasNextLine()){

           String[] data = input.nextLine().split(" ");

           int ah = Integer.parseInt(data[0]);
           int am = Integer.parseInt(data[1]);

           String hora = String.format("%02d", (ah / 30));
           String minuto = String.format("%02d", (am / 6));

           System.out.println(horas + ":" + minuto);
        }

        input.close();
	}
}