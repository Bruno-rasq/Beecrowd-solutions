import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(system.in);

        int n = in.nextInt();
        in.nextLine();
        String[] words = in.nextLine().split(' ');
        String response = "";

        for(int i = 0; i < n; i++){
            String word = words[i];

            if(!response.isEmpty()){ response += ' '; }

            if(word.length() == 3){
                if(word.startsWith("OB")){
                    response += 'OBI';
                    continue;
                }
                if(word.startsWith("UR")){
                    response += 'URI';
                    continue;
                }
            }
            response += word;
        }

        System.oout.println(response);
        in.close();
    
    }
}