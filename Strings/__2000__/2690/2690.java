import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] crypt = {
            {"GQaku", "0"},
            {"ISblv", "1"},
            {"EOYcmw", "2"},
            {"FPZdnx", "3"},
            {"JTeoy", "4"},
            {"DNXfpz", "5"},
            {"AKUgq", "6"},
            {"CMWhr", "7"},
            {"BLVis", "8"},
            {"HRjt", "9"}
        };

        int n = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < n; i++) {
            String frase = sc.nextLine();
            StringBuilder incrypt = new StringBuilder();

            for (char ch : frase.toCharArray()) {
                if (ch == ' ') continue;

                for (String[] c : crypt) {
                    if (c[0].indexOf(ch) != -1) {
                        incrypt.append(c[1]);
                        break;
                    }
                }

                if (incrypt.length() >= 12) break;
            }

            System.out.println(incrypt.substring(0, Math.min(12, incrypt.length())));
        }
    }
}