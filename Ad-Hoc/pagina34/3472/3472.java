import java.util.Scanner;
import java.util.Vector;
import java.io.IOException;

public class Main {

    static Vector<String> criancas = new Vector<String>();

    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        int n, index = 0;

        n = in.nextInt() - 1;

        criancas.add("joao");
        criancas.add("joao");

        for(int i= 0; i < n; i++){
            criancas.add("crianca" + i);
            criancas.add("crianca" + i);
        }

        while(criancas.size() > 1){
            index = (index + 28) % criancas.size();
            criancas.remove(index);
        }

        if(criancas.get(0).equal("joao")){
            System.out.println("vai ganhar");
        } else {
            System.out.println("nao vai ganhar");
        }

        in.close();
    }
}