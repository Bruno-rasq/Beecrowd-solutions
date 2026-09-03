import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] data = in.nextLine().split(" ");
        double[] dataConv = new double[3];

        for(int i = 0; i < 3; i++)
            dataConv[i] = Double.parseDouble(data[i]);

        Arrays.sort(dataConv);
        double A = dataConv[2];
        double B = dataConv[1];
        double C = dataConv[0];

        double a2 = A * A;
        double bc2 = (B * B) + (C * C);

        if(A >= B + C){ System.out.println("NAO FORMA TRIANGULO");} 
        else {
            if(Math.abs(a2 - bc2) < 1e-9 ){ System.out.println("TRIANGULO RETANGULO");}
            if(a2 > bc2){ System.out.println("TRIANGULO OBTUSANGULO");}
            if(a2 <  bc2){ System.out.println("TRIANGULO ACUTANGULO");}
            if(A == B && B == C){ System.out.println("TRIANGULO EQUILATERO");}
            else if(A == B || A == C || C == B){
                System.out.println("TRIANGULO ISOSCELES");
            }
        }

        in.close();
    }
}