import java.util.Scanner;

public class Main {

    static int calls = 0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integar.parseInt(in.nextLine());

        for (int i = 0; i < testCases; i++){
            int n = Integar.parseInt(in.nextLine());
            calls = 0;

            int output = fib(n);
            System.out.println("fib(" + n + ") = " + calls + " calls = " + output);
        }
        in.close();
    }

    public static int fib(int n){
        if (n == 1 || n == 0) return n;
        calls += 2;
        return fib(n - 1) + fib(n - 2);
    }
}