import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()){
            String line = in.nextLine();
            System.out.println(fixText(line));
        }
        in.close();
    }

    public static String fixText(String text) {
        String fixed = "";
        for (int i = 0; i < text.length(); i++) {
            char charac = text.charAt(i);
            if (i < text.length() - 1) {
                char next = text.charAt(i + 1);
                if (charac == ' ' && (next == ',' || next == '.')) {
                    continue;
                }
            }
            fixed += charac;
        }
        return fixed;
    }
}