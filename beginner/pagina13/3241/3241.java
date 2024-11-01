import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        in.nextInt();

        for(int i = 0; i < n; i++){
            String curr = in.nextLine();

            if(curr.equals("P=NP")){
                System.out.println("skipped");
                continue;
            }

            String[] data = curr.split("\\+");
            int a = Integer.parseInt(data[0]);
            int b = Integer.parseInt(data[1]);

            System.out.println(a + b);
        }

        in.close();
    }
}