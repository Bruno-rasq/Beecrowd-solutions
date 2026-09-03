import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int h1 = in.nextInt();
        int m1 = in.nextInt();
        int h2 = in.nextInt();
        int m2 = in.nextInt();

        int hr, min;

        if(h2 < h1 || (h2 == h1 && m2 < m1)){
            h2 += 24;
        }

        if(m2 < m1){
            m2 += 60;
            h2 -= 1;
        }

        hr = h2 - h1;
        min = m2 - m1;

        if(hr == 0 && min == 0){
            hr = 24;
            min = 0;
        }

        System.out.println("O JOGO DUROU "  + hr + " HORA(S) E "  + min + " MINUTO(S)");

        in.close();
    }
}