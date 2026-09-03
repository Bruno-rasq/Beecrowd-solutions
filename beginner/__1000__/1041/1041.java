import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        float a = in.nextFloat();
        float b = in.nextFloat();

        if(a == 0.0 && b == 0.0){System.out.println("Origem");}
        else if (a == 0.0){System.out.println("Eixo Y");}
        else if (b == 0.0){System.out.println("Eixo X");}
        else if (b > 0.0 && a > 0.0){System.out.println("Q1");}
        else if (b > 0.0 && a < 0.0){System.out.println("Q2");}
        else if (b < 0.0 && a < 0.0){System.out.println("Q3");}
        else if (b < 0.0 && a > 0.0){System.out.println("Q4");}

        in.close();
    }
}