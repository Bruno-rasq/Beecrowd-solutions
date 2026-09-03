import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] arg) throws IOException {
        Scanner in = new Scanner(System.in);

        int m = in.nextInt();
        int c1 = in.nextInt();
        int c2 = in.nextInt();
        int c3 = m - (c1 + c2);

        int eldest = c1;
        
        if(c2 > eldest){ eldest = c2; }
        if(c3 > eldest){ eldest = c3; }

        System.out.println(eldest);

        in.close();
    }
}