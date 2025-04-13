import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String[] data = in.nextLine().split(" ");
        
        int volume_atual = Integer.parseInt(data[0]);
        int n = Integer.parseInt(data[1]);
        
        String[] trocas = in.nextLine().split(" ");
        for(int i = 0; i < n; i++){
            int alt = Integer.parseInt(trocas[i]);
            int novo_volume = Math.max(0, Math.min(100, volume_atual + alt));
            volume_atual = novo_volume;
        }
        
        System.out.println(volume_atual);
        in.close();
    }
}