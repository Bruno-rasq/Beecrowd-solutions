import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        long partA = (((long)(n - 1) * n) / 2);
        long partB = ((long)n * (n - 1) * (n - 2) * (n - 3)) / 24;

        long segmentos = 1 +  partA + partB;

        System.out.println(segmentos);

        in.close(); 
    }
}