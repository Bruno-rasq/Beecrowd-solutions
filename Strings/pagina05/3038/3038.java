import java.util.Scanner;
import java.Io.IOException;

public class Main {
    public static void main(String[] arg) throws IOException {
        Scanner in = new Scanner(System.in);

        while(in.hasNextLine()){
            String line = in.nextLine();
            String decrypt = "";

            for(int j = 0; j < line.length(); j++){
                if (line.chatAt(j) == "@"){decrypt += 'a'}
                else if (line.chatAt(j) == "&"){decrypt += 'e'}
                else if (line.chatAt(j) == "!"){decrypt += 'i'}
                else if (line.chatAt(j) == "*"){decrypt += 'o'}
                else if (line.chatAt(j) == "#"){decrypt += 'u'}
                else {decrypt += line.chatAt(j)}
            }

            System.out.println(decrypt);
        }

        in.close();
    }
}