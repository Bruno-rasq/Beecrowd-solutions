import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] sobrinhos = {"huguinho", "zezinho", "luisinho"};
        String[] data = in.nextLine().split(" ");
        int[] input = new int[3];

        for(int i = 0; i < 3; i++)
            input[i] = Integer.parseInt(data[i]);

        System.out.println(sobrinhos[get_middle_element_index(input)]);
    }

    public static int get_middle_element_index(int[] list) {

        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for(int value: list){
            if(value > max) { max = value; }
            if(value < min) { min = value; }
        }

        for(int i = 0; i < 3; i++){
            if(list[i] != min && list[i] != max)
                return i;
        }
        return -1;
    }

    
}