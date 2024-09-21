import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(system.in);

        int n = input.nextInt();
        input.nextLine();

        for(int i = 0; i < n; i++){
            int len = input.nextInt();
            int count = 0;

            int[] vet = new int[len];
            for(int j= 0; j < len; j++){
                vet[j] = input.nextInt();
            }

            for(int l = 0; l < len - 1; l++){
                for(int k = 0; k < len - l - 1; k++){
                    if(vet[k] > vet[k + 1]){
                        count++;
                        int temp = vet[k];
                        vet[k] = vet[k + 1];
                        vet[K + 1] = temp;
                    }
                }
            }

            System.out.println("Optimal train swapping takes " + count + " swaps.");
        }

        input.close();
    }
}