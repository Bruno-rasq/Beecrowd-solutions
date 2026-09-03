import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        while(in.hasNextInt()){
            int ano = in.nextInt();

            if(ano <= 100){
                System.out.println(1);
            } else {

                int seculo = ano / 100;
                if(ano % 100 != 0){
                    seculo++;
                }

                System.out.println(seculo);
            }
        }
    }
}