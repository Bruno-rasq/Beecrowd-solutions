import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int casos = in.nextInt();
        while(casos != 0){
            String response = "";
            int menor = 0;

            for(int i = 0; i < casos; i++){
                String planet = in.next();
                int ano = in.nextInt();
                int duracao = in.nextInt();

                if(menor == 0){
                    response = planet;
                    menor = ano - duracao;
                } else {
                    if ((ano - duracao) < menor){
                        response = planet;
                        menor = ano - duracao;
                    }
                }
            }

            System.out.println(response);
            casos = in.nextInt();
        }

        in.close();
    }
}