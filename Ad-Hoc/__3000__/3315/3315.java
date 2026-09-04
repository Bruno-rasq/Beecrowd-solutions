import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int mnv = 0;
        for(int i = 0; i < 4; i++){
            String[] data = in.nextLine().split(" ");
            int soma = 0;
            for(int  j = 0; j < 7; j++){
                soma += Integer.parseInt(data[j]);
            }

            if(soma > mnv) mnv = soma;
        }

        System.out.println(mnv + " = " + Integer.toBinaryString(mnv));
    }

}