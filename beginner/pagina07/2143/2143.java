import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int t = in.nextInt();
        while(t != 0){
            for(int i = 0; i < t; i++){
                int n = in.nextInt();
                System.out.println((n - 1) % 2 == 0 ? 2 * n - 1: 2 * n - 2 );
            }
            t = in.nextInt();
        }
        in.close();
    }
}