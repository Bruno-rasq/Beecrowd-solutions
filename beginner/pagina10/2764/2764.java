import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);

        while(input.hasNextLine()){
            String[] data = input.nextLine().split('/');

            System.out.println(data[1]+"/"+data[0]+"/"+data[2]);
            System.out.println(data[2]+"/"+data[1]+"/"+data[0]);
            System.out.println(data[0]+"-"+data[1]+"-"+data[2]);
        }

        input.close();
    }
}