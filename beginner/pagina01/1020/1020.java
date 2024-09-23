import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        int age = num / 365;
        int rest = (num - (365 * age));

        int month = (rest / 30);
        int days = (rest - (30 * month));

        System.out.println(age + " ano(s)");
        System.out.println(month + " mes(es)");
        System.out.println(days + " dia(s)");
    }
}