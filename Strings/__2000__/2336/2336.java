import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long MOD = 1000000007;

        while (input.hasNextLine()) {
            String abc = input.nextLine().trim();
            long resultado = 0;

            for (char chr : abc.toCharArray()) {
                int code = chr - 'A';
                resultado = (resultado * 26 + code) % MOD;
            }

            System.out.println(resultado);
        }

        input.close();
    }
}
