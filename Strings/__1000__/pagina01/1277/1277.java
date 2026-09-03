import java.util.Scanner;
import java.util.Vector;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int casos = Integer.parseInt(in.nextLine());
        
        for(int i = 0; i < casos; i++){
            int n_alunos = Integer.parseInt(in.nextLine());
            String[] alunos = in.nextLine().split(" ");
            String[] alunos_frequencias = in.nextLine().split(" ");
            Vector<String> output = new Vector<>();
            
            for(int j = 0; j < n_alunos; j++){
                String aluno = alunos[j];
                String frequencias = alunos_frequencias[j];
                
                int total = 0, faltas = 0;
                for(char f : frequencias.toCharArray()){
                    if(f == 'M') continue;
                    if(f == 'A') faltas++;
                    total++;
                }

                if (total == 0) continue; // evita divisão por zero

                float presencas = total - faltas;
                float porcentagem = (presencas * 100.0f) / total;
                
                if (porcentagem < 75) {
                    output.add(aluno);
                }
            }

            for (int j = 0; j < output.size(); j++) {
                System.out.print(output.get(j));
                if (j < output.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        in.close();
    }
}