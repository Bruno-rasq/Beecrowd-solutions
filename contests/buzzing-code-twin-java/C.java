import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        int testeCases = Integar.parseInt(in.nextLine());

        for(int i = 0; i < testCases; i++){
            String line = in.nextLine();
            String[] data = line.split("");

            StringBuilder filteredData = new StringBuilder();
            for(String ch : data){
                if(ch.equals("<") || ch.equals(">")) filteredData.append(ch);
            }

            int diamonds = 0;
            int openCount = 0;

            for (int j = 0; j < filteredData.length(); j++){
                if(filteredData.charAt(j) == '<'){
                    openCount++;
                } else if(filteredData.charAt(j) == '>'){
                    if(openCount > 0){
                        openCount--;
                        diamonds++;
                    }
                }
            }

            System.out.println(diamonds);

        }
        in.close();
    }
}