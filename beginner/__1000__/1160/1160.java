import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(system.in);
        int n = in.nextInt();
        in.nextLine();

        for(int i = 0; i < n; i++){
            float ga, gb;
            int pa, pb;

            pa = in.nextInt();
            pb = in.nextInt();
            ga = in.nextFloat();
            gb = in.nextFloat();

            ga /= 100;
            gb /= 100;

            String response = crescimento_populacional(pa, pb, ga, gb);

            System.out.println(response);
        }
        in.close();
    }

    public static String crescimento_populacional(int pa, int pb, float ga, float gb){
        int result = 1;
        for(int i = 1; i < 101; i++){
            if(pa > pb){ break; }

            pa += (int)(pa * ga);
            pb += (int)(pb * gb);

            result += 1;
        }

        if(pa <= pb){
            return "Mais de 1 seculo.";
        } else {
            return (result - 1) + " anos.";
        }
    }
}