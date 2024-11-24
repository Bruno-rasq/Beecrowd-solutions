import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(system.in);

        String line = in.nextLine();
        String response = "";

        if(line.contains("13")){
            response = line + " es de Mala Suerte";
        } else {
            response = line + " NO es de Mala Suerte";
        }

        System.out.println(response);

        in.close();
    }
}