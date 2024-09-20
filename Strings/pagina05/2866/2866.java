import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        
        Scanner input = new Scanner(System.in);
        
        int n = input.nextInt();
        input.nextLine();

        for (int i = 0; i < n; i++) {
            String cryp = input.nextLine();
            StringBuilder descryp = new StringBuilder();

            for (int j = 0; j < cryp.length(); j++) {
                char currentChar = cryp.charAt(j);
                if (!Character.isUpperCase(currentChar)) {
                    descryp.append(currentChar);
                }
            }

            System.out.println(descryp.reverse().toString());
        }

        input.close();
    }
}
