import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(reader.readLine());
        
        int cen = n / 100;
        int rest100 = n % 100;
        
        int cin = rest100 / 50;
        int rest50 = rest100 % 50;
        
        int vin = rest50 / 20;
        int rest20 = rest50 % 20;
        
        int dez = rest20 / 10;
        int rest10 = rest20 % 10;
        
        int cinco = rest10 / 5;
        int rest5 = rest10 % 5;
        
        int dois = rest5 / 2;
        int rest2 = rest5 % 2;
        
        int um = rest2;
        
        System.out.println(n);
        System.out.printf("%d nota(s) de R$ 100,00%n", cen);
        System.out.printf("%d nota(s) de R$ 50,00%n", cin);
        System.out.printf("%d nota(s) de R$ 20,00%n", vin);
        System.out.printf("%d nota(s) de R$ 10,00%n", dez);
        System.out.printf("%d nota(s) de R$ 5,00%n", cinco);
        System.out.printf("%d nota(s) de R$ 2,00%n", dois);
        System.out.printf("%d nota(s) de R$ 1,00%n", um);
    }
}
