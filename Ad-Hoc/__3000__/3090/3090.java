import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        String[] input = in.nextLine().split(" ");
        int comprimento = Integer.parseInt(input[0]);
        int largura = Integer.parseInt(input[1]);
        int nsoldados = Integer.parseInt(input[2]);

        int hemisferioNorte = 0;
        int hemisferioSul = 0;

        double coeficiente = (float)largura / comprimento;
        for(int i = 0; i < nsoldados; i++){
            String[] data = in.nextLine().split(" ");
            int x = Integer.parseInt(data[0]);
            int y = Integer.parseInt(data[1]);
            int poder = Integer.parseInt(data[2]);

            if(y > coeficiente * x){ hemisferioNorte += poder;} 
            else {hemisferioSul += poder;}
        }

        System.out.println(hemisferioNorte + " " + hemisferioSul);
        in.close();
    }
}