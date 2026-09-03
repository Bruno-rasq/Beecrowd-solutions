import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        in.nextLine();
        for(int i = 1; i < n + 1; i++){
            String curr = in.nextLine();
            System.out.println("resposta " + i + ": " + curr);
        }

        in.close();
    }
}