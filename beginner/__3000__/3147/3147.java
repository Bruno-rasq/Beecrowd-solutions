import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		
        Scanner input = new Scanner(System.in);

        String[] data = input.nexLine().split(" ");

        int h = Integer.parseInt(data[0]);
        int e = Integer.parseInt(data[1]);
        int a = Integer.parseInt(data[2]);
        int o = Integer.parseInt(data[3]);
        int w = Integer.parseInt(data[4]);
        int x = Integer.parseInt(data[5]);

        if( (h + a + e + x) >= (o + w) ){
            System.out.println("Middle-earth is safe.");
        } else {
            System.out.println("Sauron has returned.");
        }


        input.close();
	}
}