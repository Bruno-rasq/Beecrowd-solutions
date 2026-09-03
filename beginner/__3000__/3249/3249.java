import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int wins = 0;

        in.nextLine();

        for(int i = 0; i < n; i++){
            String curr = in.nextLine();
            if(!curr.contains("CD")){
                wins++;
            }
        }

        System.out.println(wins);
        in.close();
    }
}