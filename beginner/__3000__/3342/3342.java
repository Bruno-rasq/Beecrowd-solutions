import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scannner in = new Scanner(System.in);

        int n = in.nexInt();

        int total_cases = n * n;
        int b = 0; 
        int p = 0;

        if (n % 2 == 0){
            b = total_cases / 2;
            p = total_cases / 2;
        } else {
            b = (total_cases + 1) / 2;
            p = b - 1;
        }

        System.out.println(b + " casas brancas e " p + " casas pretas");
        in.close();
    }
}