import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner (System.in);

        String[] input = in.nextLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);

        Boolean resultado = x >= 0 && x <= 432 && y >= 0 && y <= 468;

        if(resultado){
            System.out.println("dentro");
        } else {
            System.out.println("fora");
        }

        in.close();
    }
}