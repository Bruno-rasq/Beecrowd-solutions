import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{

        Scanner in = new Scanner(System.in);

        int n = in.nexInt();
        int carrinhos = 0, bonecas = 0;

        for(int i = 0; i < n; i++){
            String[] entrada = in.nextLine().split(' ');

            if(entrada[1].equals("M")){ carrinhos++; }
            else { bonecas++; }
        }

        System.out.println(carrinhos + " carrinhos");
        System.out.println(bonecas + " bonecas");

        in.close();

    }
}