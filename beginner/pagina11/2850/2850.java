import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(system.in);

        while(in.hasNextLine()){
            String entrada = in.nextLine();
            if(entrada.equals("esquerda")){System.out.println( "ingles"); }
            if(entrada.equals("direita")){ System.out.println("frances"); }
            if(entrada.equals("nenhuma")){ System.out.println("portugues"); }
            if(entrada.equals("as duas")){ System.out.println("caiu"); }
        }

        in.close();
    }
}