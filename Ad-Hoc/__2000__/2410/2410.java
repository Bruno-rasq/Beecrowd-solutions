import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        Map<Integer, Boolean> notas = new HashMap<>();

        int n = Integer.parseInt(in.nextLine());
        for(int i = 0; i < n; i++){
            int curr = Integer.parseInt(in.nextLine());
            notas.put(curr, true);
        }

        System.out.println(notas.size());
    }
}