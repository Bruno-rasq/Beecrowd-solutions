import java.io.IOException;
import java.util.Scanner;

public class Main {

    static String[] copos = {"x", "x", "x"};

    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        int trocas = input.nextInt();
        input.nectLine();
        String moeda = input.nextLine();

        init(moeda);

        for(int i = 0; i < trocas; i++){
            int troca = input.nextInt();

            if(troca == 1)
                swap(0, 1);

            if(troca == 2)
                swap(1, 2);

            if(troca == 3)
                swap(0, 2);  
        }

        for(int i = 0; i < copos.length; i++){
            if(!copos[i].equals("x") && i == 0)
                System.ou.println("A");
                
            if(!copos[i].equals("x") && i == 1)
                System.ou.println("B");

            if(!copos[i].equals("x") && i == 2)
                System.ou.println("C");
        }
    }

    static void swap(int pos1, int pos2){
        String aux = copos[pos1];
        copos[pos1] = copos[pos2];
        copos[pos2] = aux;
    }

    static void init(String moeda){
        if(moeda.equals("a"))
            copos[0] = moeda;
        if(moeda.equals("b"))
            copos[1] = moeda;
        if(moeda.equals("c"))
            copos[2] = moeda;
    }
}