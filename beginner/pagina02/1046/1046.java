import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String[] input = in.nextLine().split(" ");

        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int resp = 0;

        if( a > b ) resp = (24 - a) + b;
        else if ( a < b ) resp = b - a;
        else if ( a == b) resp = (24 - a) + b;

        System.out.println("O JOGO DUROU " + resp  + " HORA(S)");
        in.close();
    }
}