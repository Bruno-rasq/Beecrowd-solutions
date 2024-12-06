import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(system.in);

        while(in.hasNextLine()){
            String becteria_dna = in.nextLine();
            String code_genetico = in.nextLine();

            if(becteria_dna.contains(code_genetico)){
                System.out.println("Resistente");
            } else {
                System.out.println("Nao resistente");
            }
        }
        in.close();
    }
}