import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int casos = scanner.nextInt();
        
        while (casos != 0) {
            String response = "";
            int menor = 0;
            
            for (int i = 0; i < casos; i++) {
                String planeta = scanner.next();
                int ano = scanner.nextInt();
                int duracao = scanner.nextInt();
                
                if (menor == 0) {
                    response = planeta;
                    menor = ano - duracao;
                } else {
                    if ((ano - duracao) < menor) {
                        response = planeta;
                        menor = ano - duracao;
                    }
                }
            }
            
            System.out.println(response);
            casos = scanner.nextInt();
        }
        
        scanner.close();
    }
}