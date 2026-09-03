import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);

        float notas = new Float[4];
        String[] innotas = in.nextLine().split(" ");

        for(int i = 0; i < 4; i++){
            notas[i] = Float.parseFloat(innotas[i]);
        }

        double media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + (notas[3] * 1)) / 10;

        system.out.println("Media: " + String.format("5.1f", media));

        if (media >= 7.0){

            system.out.println("Aluno aprovado.");
        }
        else if (media < 5.0){

            system.out.println("Aluno reprovado.");
        }
        else{
            float exame = in.nextfloat();

            system.out.println("Aluno em exame.");
            system.out.println("Nota do exame: " + exame);

            double mediaComExame = (media + exame) / 2;

            if (mediaComExame >= 5.0){
                system.out.println("Aluno aprovado.");
            }
            else{
                system.out.println("Aluno reprovado.");
            }

            system.out.println("Media final: " + mediaComExame);
        }
        in.close();
    }
}