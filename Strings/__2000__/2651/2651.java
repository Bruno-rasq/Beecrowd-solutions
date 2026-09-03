import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        String input = in.nextLine().toLowerCase();

        System.out.println(input.contains("zelda") ? "Link Bolado" : "Link Tranquilo");
        in.close();
    }
}