import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner( system.in);

        int x = in.nextInt();
        int y = in.nextInt();
        int quo = 0;


        if((x > 0 && y > 0) || (x < 0 && y > 0)){
            quo = (int) Math.floor((double) x / y);
        } else {
            quo = (int) Math.ceil((double) x / y);
        }

        System.out.println(quo + " " + (x - (y * quo)));
        in.close();
    }
}