import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws IOException {
        
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.nextLine();
        int gifts = 0;
        int restB = 0, restA = 0, restM = 0, restD = 0;

        for(int i = 0; i < n; i++){
            String[] data = input.nextLine().split(" ");
            int hours = Integer.parseInt(data[2]);

            if(data[1].equals('bonecos')){
                gifts += (hours + restB) / 8
                restB = (hours + restB) % 8
            }
            if(data[1].equals('arquitetos')){
                gifts += (hours + restA) / 4
                restA = (hours + restA) % 4
            }
            if(data[1].equals('musicos')){
                gifts += (hours + restM) / 6
                restM = (hours + restM) % 6
            }
            if(data[1].equals('desenhistas')){
                gifts += (hours + restD) / 12
                restD = (hours + restD) % 12
            }
        }

        System.out.println(gifts);

        input.close();
	}
}