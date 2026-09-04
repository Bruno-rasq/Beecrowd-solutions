import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int i1 = in.nextInt();
        int i2 = in.nextInt();

        if(((i1 >= 14 && i2 >= 14) || (i1 >= 18 || i2 >= 18)) && i1 >= 6 && i2 >= 6){
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        in.close();
    }
}