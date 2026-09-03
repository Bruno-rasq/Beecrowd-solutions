import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        String[] data = in.nextLine().split(" ");
        int x1 = Integer.parseInt(data[0]);
        int y1 = Integer.parseInt(data[1]);
        int x2 = Integer.parseInt(data[2]);
        int y2 = Integer.parseInt(data[3]);

        int i = 1;
        while(x1 != 0 && y1 != 0 && x2 != 0 && y2 != 0){
            int n, meteoros = 0;
            n = Integer.parseInt(in.nextLine());

            for(int j = 0; j < n; j++){
                int x, y;
                String[] curr = in.nextLine().split(" ");
                x = Integer.parseInt(curr[0]);
                y = Integer.parseInt(curr[1]);
                if (x1 <= x && x <= x2 && y2 <= y && y <= y1) {
                    meteoros++;
                }
            }

            System.out.println("Teste " + i);
            System.out.println(meteoros);

            i++;
            String[] next = in.nextLine().split(" ");
            x1 = Integer.parseInt(next[0]);
            y1 = Integer.parseInt(next[1]);
            x2 = Integer.parseInt(next[2]);
            y2 = Integer.parseInt(next[3]);
        }
        in.close();
    }
}