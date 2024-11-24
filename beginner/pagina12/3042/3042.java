import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(system.in);

        int n = in.nextInt();
        in.nextLine();

        while (n > 0){
            int posicaoAtual = 2;
            int contador = 0;

            for(int i = 0; i < n; i++){
                Strinha linha = in.nextLine();

                if(linha.equals("0 1 1") && posicaoAtual != 1){
                    contador += Math.abs(posicaoAtual - 1);
                    posicaoAtual = 1;
                }
                else if(linha.equals("1 0 1") && posicaoAtual != 2){
                    contador += Math.abs(posicaoAtual - 2);
                    posicaoAtual = 2;
                }
                else if(linha.equals("1 1 0") && posicaoAtual != 3){
                    contador += Math.abs(posicaoAtual - 3);
                    posicaoAtual = 3;
                }
            }

            System.out.println(contador);
            n = in.nextInt();
            in.nextLine();
        }
        in.close();
    }
}