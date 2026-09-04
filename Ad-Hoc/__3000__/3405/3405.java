import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(trailling_zeros(n));
        in.close();

    }

    public static int trailling_zeros(int n){
        int count = 0;
        while (n >= 5){
            n = (int) Math.floor((double) n / 5);
            count += n;
        }
        return count;
    }
}