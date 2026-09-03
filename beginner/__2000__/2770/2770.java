import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        StringBuilder output = new StringBuilder();

        while(in.hasNextInt()){

            int lp = in.nextInt();
            int ap = in.nextInt();
            int qnt = in.nextInt();

            for(int i = 0; i < qnt; i++){
                int lpc = in.nextInt();
                int apc = in.nextInt();

                if((lpc <= lp && apc <= ap) || (lpc <= ap && apc <= lp)){
                    output.append("Sim\n");
                } else {
                    output.append("Nao\n");
                }
            }
        }

        System.out.print(output);
        in.close();
    }
}