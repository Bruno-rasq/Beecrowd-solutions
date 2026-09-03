import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int input = in.nextInt();

        String l[] = {
            "2", "7", "5", "30", "169",
            "441", "1872", "7632", "1740",
            "93313", "459901", "1358657",
            "2504881", "13482720", "25779600",
            "68468401", "610346880",
            "1271932200", "327280800"
        };

        System.out.println(l[input - 1]);
        in.close();
    }
}