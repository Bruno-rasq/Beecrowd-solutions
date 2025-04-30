import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        
        Scanner in = new Scanner(System.in);
        int max = Integer.MAX_VALUE;
        
        while (in.hasNextLine()) {
            String n = in.nextLine();
            StringBuilder num = new StringBuilder();
            boolean isValid = true;
            
            for (int i = 0; i < n.length(); i++) {
                char chr = n.charAt(i);
                
                if (chr >= '0' && chr <= '9') {
                    num.append(chr);
                } else if (chr == 'O' || chr == 'o') {
                    num.append('0');
                } else if (chr == 'l') {
                    num.append('1');
                } else if (chr == ' ' || chr == ',') {
                    continue;
                } else {
                    isValid = false;
                    break;
                }
            }

            String result = num.toString().replaceFirst("^0+(?!$)", ""); // remove zeros à esquerda
            boolean error = result.isEmpty();

            if (!error) {
                try {
                    long parsed = Long.parseLong(result);
                    if (parsed > max) error = true;
                } catch (NumberFormatException e) {
                    error = true;
                }
            }

            System.out.println(!error && isValid ? result : "error");
        }

        in.close();
    }
}