import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        in.nextLine();

        for(int i = 0; i < n; i++){
            String[] input = in.nextLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);

            int step = steps(a, b);
            System.out.println("Case " + (i + 1) + ": " + (step + 1));
        }
        in.close();
    }

    public static int steps(int n, int k){
        int result = 0;
        for(int i = 2; i < n + 1; i++){
            result = (result + k) % i;
        }
        return result;
    }
}