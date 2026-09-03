import java.util.Scanner;

public class Main {
    static int possibilidades[] = {
        0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 
        1588356, 8676360, 47977776, 266378112, 1488801600
    };
    
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        
        int n = Integer.parseInt(in.nextLine());
        
        for(int i = 0; i < n; i++){
            int curr = Integer.parseInt(in.nextLine()) - 1;
            System.out.println(possibilidades[curr]);
        }
    }
}