import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());

        int soma = 0;
        for (int i = 0; i < n; i++) {
            String line = in.nextLine();
            String digits = "";

        
            for (int j = 0; j < line.length(); j++) {
                char c = line.charAt(j); 
                if (Character.isDigit(c)) digits += c;
            }

            
            soma += Integer.parseInt(digits);
        }

        System.out.println(soma);
        in.close();
    }
}
