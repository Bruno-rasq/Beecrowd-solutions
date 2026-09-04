import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        ArrayList<Float> medias = new ArrayList<>();
        int i = 0;

        while(in.hasNextLine()){

            String data[] = in.nextLine().split(" ");
            int w1 = Integer.parseInt(data[0]);
            int w2 = Integer.parseInt(data[1]);
            int reps = Integer.parseInt(data[2]);

            if(w1 == 0 && w2 == 0 && reps == 0) break;

            float w1_max = rep_maxima(w1, reps);
            float w2_max = rep_maxima(w2, reps);
            float media_rm = (w1_max + w2_max) / 2.0f;

            medias.add(media_rm);

            if (1 <= media_rm && media_rm < 13) {
                System.out.println("Nao vai da nao");
            } else if (13 <= media_rm && media_rm < 14) {
                System.out.println("E 13");
            } else if (14 <= media_rm && media_rm < 40) {
                System.out.println("Bora, hora do show! BIIR!");
            } else if (40 <= media_rm && media_rm <= 60) {
                System.out.println("Ta saindo da jaula o monstro!");
            } else {
                System.out.println("AQUI E BODYBUILDER!!");
            }

            i++;
        }

        float media_geral = calcular_media_geral(medias);

        if(media_geral > 40.0){
            System.out.println();
            System.out.println("Aqui nois constroi fibra rapaz! Nao e agua com musculo!");
        }
        in.close();
    }

    public static float rep_maxima(int peso, int reps){
        return peso * (1 + (reps / 30.0f));
    }

    public static float calcular_media_geral(ArrayList<Float> medias){
        float soma = 0.0f;
        for (float media : medias) {
            soma += media;
        }

        return soma / medias.size();
    }
}
