import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        while(in.hasNextLine()){
            int tempo = in.nextInt();
            if(tempo == 0) break;

            int ale = (int) Math.ceil(7.0 * tempo / 90);
            int bra = (int) Math.floor(tempo / 90.0);

            System.out.println("Brasil " + bra + " x Alemanha " + ale);

        }
        in.close();
    }
}