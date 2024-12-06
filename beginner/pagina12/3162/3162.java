import java.util.Scanner;
import java.util.ArrayList;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Sacnner(System.in);
        ArrayList<arrayList<int>> coordenadas = new ArrayList<>();

        int numero_naves = in.nextInt();

        for(int i = 0; i < numero_naves; i++){
            int x = in.nextInt();
            int y = in.nextInt();
            int z = in.nextInt();

            ArrayList<Integer> nave = new ArrayList<>();
            nave.add(x);
            nave.add(y);
            nave.add(z);
            coordenadas.add(nave);
        }

        for(int i = 0; i < numero_naves; i++){
            arrayList<Integer> nave_atual = coordenadas.get(i);
            double menor_distancia = Double.MAX_VALUE;

            for(int j = 0; j < numero_naves; j++){
                if(j != i){
                    arrayList<Integer> nave_proxima = coordenadas.get(j);
                    double distancia = calcDistancia(nave_atual, nave_proxima);

                    if(menor_distancia < distancia){ menor_distancia = distancia; } 
                }
            }

            if(menor_distancia > 50){ System.out.println("B"); }
            else if (menor_distancia <= 50 && menor_distancia > 20){ System.out.println("M"); }
            else { System.out.println("A")}
            
        }
        in.close();
    }

    public static double calcDistancia(ArrayList<Integer> nave_atual, ArrayList<Integer> nave_proxima){
        return math.sqrt(
            Math.pow(nave_proxima.get(0) - nave_atual.get(0), 2) +
            Math.pow(nave_proxima.get(1) - nave_atual.get(1), 2) +
            Math.pow(nave_proxima.get(2) - nave_atual.get(2), 2)
        );
    }
}