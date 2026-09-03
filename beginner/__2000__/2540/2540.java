import java.util.Scanner;

public class Main {
    public static void main (String[] args) {

        Scanner in = new Scanner(System.in);

        while (in.hasNextInt()) {

            int jogadores = in.nextInt();
            in.nextLine();

            String[] votos = in.nextLine().split(" ");
            int votosImpeat = 0;

            for(int i = 0; i < jogadores; i++){
                if(Integer.parseInt(votos[i] == 1)){
                    votosImpeat++;
                }
            }

            double doistercos = jogadores * (2.0 / 3.0);

            System.out.println(votosImpeat >= doistercos ? "impeachment" : "acusacao arquivada");

        }

        in.close();
    }
}