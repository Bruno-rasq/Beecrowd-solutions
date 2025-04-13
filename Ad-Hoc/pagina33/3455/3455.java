import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        
        Scanner in = new Scanner(System.in);
        
        String[] data = in.nextLine().split(" ");
        String tipo = in.nextLine(); // <- faltava o ponto e vírgula aqui
        
        long grafica = Long.parseLong(data[0]);
        long dinamica = Long.parseLong(data[1]);
        long geometrica = Long.parseLong(data[2]);
        
        double total  = 0.0;
        
        if(tipo.equals("A")){
            total += grafica;
            total += dinamica * (3.0 / 2);
            total += geometrica * 2.5;
        }
        else if (tipo.equals("B")){
            total += dinamica;
            total += grafica * (2.0 / 3);
            total += geometrica * 2.5 * (2.0 / 3);
        }
        else if (tipo.equals("C")){
            total += geometrica;
            total += grafica * (1.0 / 2.5);
            total += dinamica * (3.0 / 2) * (1.0 / 2.5);
        }
        
        System.out.println((long)Math.floor(total)); // <- imprime o resultado truncado
        in.close();
    }
}