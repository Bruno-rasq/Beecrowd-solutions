import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        String str1 = input.nextLine();
        int k = Integer.parseInt(input.nextLine());

        int indice = -1;
        int menor_distancia = Integer.MAX_VALUE; // Troquei Float.POSITIVE_INFINITY() por Integer.MAX_VALUE
                                                 // pois distância de Hamming sempre será um número inteiro
                                                 // e não é necessário usar float

        for(int i = 0; i < 5; i++){
            String str2 = input.nextLine();

            int distance = hamming_distance(str1, str2);
            if(distance < menor_distancia){
                menor_distancia = distance;
                indice = i + 1;
            }
        }

        System.out.println(indice);
        System.out.println(menor_distancia <= k ? menor_distancia : -1);
    }

    public static int hamming_distance(String str1, String str2){
        int distance = 0;
        for(int i = 0; i < str1.length(); i++){ // Correção: str1.length -> str1.length()
            if(str1.charAt(i) != str2.charAt(i)){ // Correção: str1[i] -> str1.charAt(i)
                distance++;
            }
        }
        return distance;
    }
}
