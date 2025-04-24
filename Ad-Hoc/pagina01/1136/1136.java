import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Main {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);

        while (true){

            String[] data = in.nextLine().split(" ");
            int N = Integer.parseInt(data[0]);
            int B = Integer.parseInt(data[1]);

            if(N == 0 && B == 0) break;

            String[] bolas = in.nextLine().split(" ");
            Set<Integer> possibilidades = new HashSet<Integer>();

            for(int i = 0; i < B; i++){
                int bi = Integer.parseInt(bolas[i]);
                for(int j = 0; j < B; j++){
                    int bj = Integer.parseInt(bolas[j]);
                    possibilidades.add(Math.abs(bi - bj));
                }
            }

            System.out.println(possibilidades.size() >= N + 1 ? "Y" : "N");
        }

        in.close();
    }
}
