import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);

        String text = input.nextLine();

        if(text.length() <= 80){
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        input.close();
    }
}