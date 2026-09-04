import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        Set<Integer> stickers = new HashSet<Integer>();
        int n = Integer.parseInt(in.nextLine());
        int repeated_stickers = 0;

        for(int i = 0; i < n; i++){
            int sticker = Integer.parseInt(in.nextLine());
            int len = stickers.size();
            stickers.add(sticker);
            if(stickers.size() == len) repeated_stickers++;
        }

        System.out.println(stickers.size());
        System.out.println(repeated_stickers);
        in.close();
    }
}