import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);

        String nome = in.nextLine();
        String[] data1 = in.nextLine().split("/");
        String[] data2 = in.nextLine().split("/");

        int dia_atual = Integer.parseInt(data1[0]); int dia_nasci = Integer.parseInt(data2[0]);
        int mes_atual = Integer.parseInt(data1[1]); int mes_nasci = Integer.parseInt(data2[1]);
        int ano_atual = Integer.parseInt(data1[2]); int ano_nasci = Integer.parseInt(data2[2]);

        int idade = ano_atual - ano_nasci;

        if(dia_nasci == dia_atual && mes_nasci == mes_atual){
           System.out.println("Feliz aniversario!");
        }

        if(mes_atual < mes_nasci || (mes_atual == mes_nasci &&  dia_atual < dia_nasci)){
            idade -= 1;
        }

        System.out.println("Voce tem " + idade + " anos " + nome + ".");
        
    }
}