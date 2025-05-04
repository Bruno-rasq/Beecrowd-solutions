import java.util.Scanner;

public class Main {
    
    public static void main(String[] args){
        
        Scanner in = new Scanner(System.in);
        
        while(in.hasNextLine()){
            String[] frase = in.nextLine().split(" ");
            int media = media_frase(frase);
            
            System.out.println(
                media <= 3 ? 250 : (media > 3 && media <= 5 ? 500 : 1000)
            );
        }
        
        in.close();
    }
    
    public static int media_frase(String[] frase) {
        int totalPalavras = 0;
        int somatoriaPalavras = 0;
    
        for (String palavra : frase) {
            if (palavra.endsWith(".")) {
                palavra = palavra.substring(0, palavra.length() - 1);
            }
    
            if (palavra.matches("[A-Za-z]+")) {
                somatoriaPalavras += palavra.length();
                totalPalavras++;
            }
        }
    
        if (totalPalavras == 0) return 0;
        return somatoriaPalavras / totalPalavras;
    }
}
