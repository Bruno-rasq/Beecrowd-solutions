import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int total = 0;

        int[] casas = {1000000, 100000, 10000, 1000, 100, 10, 1};

        for(int i = 0; i < 7; i++){
            int casa = casas[i];
            if(n >= casa){
                int qnt = n - casa + 1;
                int digitos = Integer.toString(casa).length();
                total += qnt * digitos;
                n = casa - 1;
            }
        }

        System.out.println(total);
        input.close();
    }
}
