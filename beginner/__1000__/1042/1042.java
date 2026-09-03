import java.util.Scanner;

public class Main {
    public static void main(String[] arg) {

        Scanner in = new Scanner(System.in);

        int A = in.nextInt();
        int B = in.nextInt();
        int C = in.nextInt();

        int[] valores = {A, B, C};
        int[] valoresOrdenados = simpleSort(valores);

        for(int value: valoresOrdenados)
            System.out.println(value);

        System.out.println(" ");

        for(int value: valores)
            System.out.println(value);

        in.close();
    }

    public static int[] simpleSort(int[] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr.length - i - 1; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }
}
