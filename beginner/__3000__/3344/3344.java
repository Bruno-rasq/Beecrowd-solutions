import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        for(int i = 0; i < 1000; i++){
            n = brute(n);
        }

        System.out.println(n);
        in.close();

    }

    public static int brute(int n){

        int[] unitarios = {
            4, 3, 3, 5, 4, 4, , 3, 5, 5, 4, 3,
            6, 6, 8, 8, 7, 7, 9, 8, 8, 6
        };

        int[] decimais = {6, 6, 5, 5, 5, 7, 6, 6};

        if(n == 100){ return 11; }
        else if (n <= 20){ return unitarios[n]; }
        else {
            int dec = n / 10;
            int uni = n % 10;
            int result = decimais[dec - 2];
            if(uni != 0){
                result += unitarios[uni];
            }
            return result;
        }
    }
}