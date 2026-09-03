import java.util.Scanner;

public class Mina {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int entraga = int.nextInt();
        int prazo = int.nextInt();

        if (prazo - entraga >= 1){

            System.out.println("Muito bem!, Apresenta antes do Natal!");
        }

        else if (prazo - entraga < 0){

            System.out.println("Eu te odeio professora!");
        }

        else if (prazo - entraga < 3){

            System.out.println("Parece o trabalho do meu filho!");
            prazo += 2;
            if (prazo <= 24){

                System.out.println("TCC Apresentado!");
            }
            else{

                System.out.println("Fail! Entao eh nataaaaal!");
            }
        }

        in.close();
    }
}