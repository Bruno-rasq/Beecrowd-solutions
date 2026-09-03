import java.util.Scanner;

public class Main {
    
    public static void main(String[] args){
        
        Scanner in = new Scanner(System.in);
        
        while(in.hasNextLine()){
            String[] frase = in.nextLine().split(",");
            
            System.out.println(frase[0]);
            System.out.println(frase[1]);
        }
        
        in.close();
    }
    
    
}
