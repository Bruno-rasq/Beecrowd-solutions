import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int total_pecas = Integer.parseInt(in.nextLine());
        String[] pecas = in.nextLine().split(" ");

        for(int i = 1; i <= total_pecas; i++){

            Boolean encontrou = false;
            for(String peca: pecas){

                if(Integer.parseInt(peca) == i) {
                    encontrou = true;
                    break;
                }
            }

            if(!encontrou){
                System.out.println(i);
                break;
            }
        }
    }
}