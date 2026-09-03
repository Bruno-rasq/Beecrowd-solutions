import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        
        while (in.hasNextLine()) {
            String[] nxm = in.nextLine().split(" ");
            int n = Integer.parseInt(nxm[0]);
            int m = Integer.parseInt(nxm[1]);
            
            int[] X = new int[2];
            int[] Y = new int[2];
            
            for (int i = 0; i < n; i++) {
                String[] linha = in.nextLine().split(" ");
                for (int j = 0; j < m; j++) {
                    if (linha[j].equals("1")) {
                        X[0] = i;
                        X[1] = j;
                    } else if (linha[j].equals("2")) {
                        Y[0] = i;
                        Y[1] = j;
                    }
                }
            }
            
            int dist = Math.abs(X[0] - Y[0]) + Math.abs(X[1] - Y[1]);
            System.out.println(dist);
        }
        
        in.close();
    }
}