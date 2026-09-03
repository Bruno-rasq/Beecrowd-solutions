import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int[] moedas = new int[n];

        for(int i = 0; i < n; i++){
            int moeda = in.nextInt();
            moedas[i] = moeda;
        }

        int salto = in.nextInt();
        int resultado = contagem(moedas, salto);

        if(eh_primo(resultado)){
            System.out.println("You're a coastal aircraft. Robbie, a large silver aircraft.");
        } else {
            System.out.println("Bad boy! I'll hit you.");
        }
        in.close();
    }

    public static int contagem(int[] moedas, int salto){
        int index = moedas.size() - 1;
        int soma = 0;
        while(index >= 0){
            soma += moedas[index];
            index -= salto;
        }
        return soma;
    }

    public static boolean eh_primo(int n){
        if(n <= 1) return false;
        for(int i = 2; i <= Math.sqrt(n); i++){
            if(n % i === 0) return false;
        }
        return true;
    }
}