import jva.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int casos = in.nextInt();
        in.nextLine();

        for(int i = 0; i < casos; i++){
            int feddback_number = in.nextInt();
            in.nextLine();

            for(int j = 0; j < feddback_number; j++){
                int feed = in.nextInt();
                String output = '';

                if(feed == 1) output = "Rolien";
                if(feed == 2) output = "Naej";
                if(feed == 3) output = "Elehcim";
                if(feed == 4) output = "Odranoel";

                System.out.println(output); 

            }
        }
        in.close();
    }
}