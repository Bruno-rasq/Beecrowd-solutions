import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] input = in.nextLine().split(" ");
        int voltas = Integer.parseInt(input[0]);
        int placas = Integer.parseInt(input[1]);

        double total_placas = (double) voltas * placas;

        StringBuilder output = new StringBuilder();
        for(int i = 10 ; i <= 90; i+= 10){
            int qnt_placas = (int) Math.ceil((total_placas * i) / 100.0);
            if(output.length() > 0){
                output.append(" ");
            }
            output.append(qnt_placas);
        }

        System.out.println(output);
        in.close();
    }
}