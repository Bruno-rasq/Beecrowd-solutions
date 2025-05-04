import java.util.Scanner;

public class Main {

    static final String[] nokia_keyboard = {
        "2", "2", "2",  // a, b, c
        "3", "3", "3",  // d, e, f
        "4", "4", "4",  // g, h, i
        "5", "5", "5",  // j, k, l
        "6", "6", "6",  // m, n, o
        "7", "7", "7", "7",  // p, q, r, s
        "8", "8", "8",  // t, u, v
        "9", "9", "9", "9"   // w, x, y, z
    };

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        while (in.hasNextLine()) {
            String input = in.nextLine();
            StringBuilder output = new StringBuilder();

            for (int i = 0; i < input.length(); i++) {
                char chr = input.charAt(i);

                if (Character.isLetter(chr)) {
                    int idx = Character.toLowerCase(chr) - 'a';
                    output.append(nokia_keyboard[idx]);
                } else if (Character.isDigit(chr) || chr == '*' || chr == '#') {
                    output.append(chr);
                }
                // outros símbolos são ignorados
            }

            System.out.println(output);
        }

        in.close();
    }
}