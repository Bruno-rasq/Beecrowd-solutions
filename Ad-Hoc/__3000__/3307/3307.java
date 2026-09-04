import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for(int i = 0; i < n; i++){
            int area = in.nextInt();
            double raio = Math.sqrt(area / (4 * 3.14));

            if (raio < 12){
                double valor = area * 0.09;
                System.out.println("vermelho = R$ " + String.format("%.2f", valor));
            }
            
            else if (raio >= 12 && raio <= 15){
                double valor = area * 0.07;
                System.out.println("azul = R$ " + String.format("%.2f", valor));
            }
            
            else if (raio > 15){
                double valor = area * 0.05;
                System.out.println("amarelo = R$ " + String.format("%.2f", valor));
            }
        }
        in.close();
    }
}