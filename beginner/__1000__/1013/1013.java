import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        String[] entrada = input.nextLine().split(" ");

       
        int a = Integer.parseInt(entrada[0]);
        int b = Integer.parseInt(entrada[1]);
        int c = Integer.parseInt(entrada[2]);


        System.out.printf("%d eh o maior\n", max(a, max(b, c)));

        input.close();

    }

    public static int max(int a, int b){
        return (a + b + Math.abs(a - b)) / 2;
    }
}