import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int guardachuvaCasa = 0;
        int guardachuvatrabalho = 0;
        int comprasCasa = 0;
        int comprasTrabalho = 0;

        int n = in.nextInt();
        in.nextLine();

        for(int i = 0; i < n; i++){
            String[] input = in.nextLine().split(" ");
            String ida = input[0];
            String volta = input[1];

            if(ida.equals("chuva")){
                if(guardachuvaCasa > 0){ guardachuvaCasa--; } else { comprasCasa++; }
                guardachuvatrabalho++;
            }

            if(volta.equals("chuva")){
                if(guardachuvatrabalho > 0){ guardachuvatrabalho--; } else { comprasTrabalho++; }
                guardachuvaCasa++;
            }
        }

        System.out.println( comprasCasa + " " + comprasTrabalho);
        in.close();
    }
}