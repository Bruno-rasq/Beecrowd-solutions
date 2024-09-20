import java.io.IOException;
import java.util.Scanner;

class CircularList {

    String[] lista_de_nomes;
    int index = 0;

    CircularList(String[] lista){
        this.lista_de_nomes = lista;
    }

    String next (){
        String nome =  this.lista_de_nomes[this.index];
        this.index = (this.index + 1) % this.lista_de_nomes.length();
        return nome;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        String rico = "";
        int quantidade_de_pessoas = input.nextInt();
        double litros = input.nextDouble();
        double refill = input.nextDouble();

        String[] lista = new String[quantidade_de_pessoas];

        for(int i = 0; i < quantidade_de_pessoas; i++){
            lista[i] = input.next();
        }

        CircularList amigos = new CircularList(lista);

        while(litros > refill){
            litros -= refill;
            rico = amigos.next();
        }

        rico = amigos.next();

        System.out.println(rico + " " + String.format("%.1f", litros));

        input.close();
    }
}