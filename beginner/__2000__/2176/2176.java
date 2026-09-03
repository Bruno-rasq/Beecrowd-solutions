import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        String input = in.nextLine();
        int bits_1 = 0;

        for(int i =0 ; i < input.length(); i++){
            char bit = input.charAt(i);
            if(bit == '1'){
                bits_1 += 1;
            }
        }

        if(bits_1 % 2 == 0){
            input += "0";
        } else {
            input += "1";
        }

        System.out.println(input);
        in.close();

    }
}