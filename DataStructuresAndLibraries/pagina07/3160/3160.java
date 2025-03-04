import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] lista_atual = in.nextLine().split(" ");
        String[] nova_lista  = in.nextLine().split(" ");
        String amigo_indicado = in.nextLine();
        ArrayList<String> lista_atualizado = new ArrayList<>();
        
        if (!amigo_indicado.equals("nao") 
            && Arrays.asList(lista_atual).contains(amigo_indicado)) {
            
            for (String amigo : lista_atual) {
                if (amigo.equals(amigo_indicado)) {
                    for (String novo_amigo : nova_lista) {
                        lista_atualizado.add(novo_amigo);
                    }
                }
                lista_atualizado.add(amigo);
            }
            
        } else {
            for (String amigo : lista_atual) lista_atualizado.add(amigo);
            for (String amigo : nova_lista)  lista_atualizado.add(amigo);
        }
        
        System.out.println(String.join(" ", lista_atualizado));
        in.close();
    }
}