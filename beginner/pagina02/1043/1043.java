import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        float A = in.nextFloat();
        float B = in.nextFloat();
        float C = in.nextFloat();

        float perimetro = (A + B + C);
        float area = ((A + B) * C ) / 2;
        Boolean condicao = A < (B + C) && B < ( A + C) && C < (A + B);

        if(condicao){
            System.out.println("Perimetro = %.1f%n", perimetro);
        } else {
            System.out.println("Area = %.1f%n", area);
        }

        in.close();
    }
}