import java.util.Scanner;
import java.io.IOException;

public class Main {

    private static final double R = 0.30;
    private static final double G = 0.59;
    private static final double B = 0.11;

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);

        int numero_casos = in.nextInt();
        for(int i = 1; i <= numero_casos; i++){

            String tipo = in.nextLine();
            String[] rgb = in.nextLine().split(" ");
            int resultado = 0;

            int r = Integer.parseInt(rgb[0]);
            int g = Integer.parseInt(rgb[1]);
            int b = Integer.parseInt(rgb[2]);

            if(tipo.equals("eye")){ resultado = (int)(R * r + G * g + B * b); }
            if(tipo.equals("min")){ resultado = Math.min(r, Math.min(g, b)); }
            if(tipo.equals("max")){ resultado = Math.max(r, Math.max(g, b)); }
            if(tipo.equals("mean")){ resultado = (r + g + b) / 3;; }

            System.out.println("Caso #" + i + ": " + resultado);
        }
        in.close();
    }
}