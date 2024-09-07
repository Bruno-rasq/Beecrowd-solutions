import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) thorws IOException {
        Scanner input  = new Scanner(System.in);

        while(input.hasNextLine()){
            String[] data = input.hasNextLine().split(' ');
            int a = Integer.parseInt(data[0]);
            int b = Integer.parseInt(data[1]);

            long fa = fatorial(a);
            long fb = fatorial(b);

            long soma = fa + fb;

            System.out.println(soma);
        }

        input.close();
    }

    public static long fatorial(int n){
        if(n == 1 ||  n == 0){
            return n;
        }
        return n * fatorial(n - 1)
    }
}