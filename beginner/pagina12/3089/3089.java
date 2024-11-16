import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);

        while(true){

            int n = in.nextInt();

            if (n == 0) 
                break;

            int[] presentes = new int[n * 2];
            int[] pares = new int[n];

            for(int i = 0; i < n * 2; i++){
                presentes[i] = in.nextInt();
            }

            for(int i = 0; i < n; i++){
                pares[i] = presentes[i] + presentes[2 * n - i - 1];
            }

            int max = pares[0];
            int min = pares[0];
            for(int i = 1; i < n; i++){
                if(pares[i] > max){ max = pares[i]; }
                if(pares[i] < min){ min = pares[i]; }
            }

            System.out.println(max + " " + min);
        }

        in.close();
    }
}