import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] arg) throws IOException {
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();

        System.out.println(a % b);

        in.close();
    }
}