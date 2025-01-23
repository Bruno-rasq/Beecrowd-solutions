import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String[] input = in.nextLine().split(" ");

        int porcent1 = Integer.parseInt(input[0]);
        int porcent2 = Integer.parseInt(input[1]);

        if ( porcent2 <= 2 && porcent2 >= 0 )
            System.out.println("nova");

        else if ( porcent2 <= 100 && porcent2 >= 97 )
            System.out.println("cheia");

        else if ( porcent1 < porcent2)
            System.out.println("crescente");

        else 
            System.out.println("minguante"); 

        in.close();
    }
}