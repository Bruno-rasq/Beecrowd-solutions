import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        int horas = num / 3600;
        int minutos = (num % 3600) / 60;
        int segundos = num % 60;

        System.out.println(horas + ":" + minutos + ":" + segundos);
    }
}
