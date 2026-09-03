import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        int linha, coluna;
        Scanner input = new Scanner(System.in);

        linha = input.nextInt();
        coluna = input.nextInt();

        if(verification(linha, coluna)){
            System.out.println(1);
        } else {
            System.out.println(0);
        }

    }

    static Boolean isEven(int num){
        return num % 2 == 0;
    }

    static Boolean verification(int linha, int coluna){
        return (isEven(linha) && isEven(coluna)) || (!isEven(linha) && !isEven(coluna));
    }
}