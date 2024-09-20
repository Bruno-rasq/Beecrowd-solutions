import java.io.IOException;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) throws IOException {
		Scanner input = new Canner(System.in);

        Boolean tag = false;
        String line;

        while(input.hasNextLine()){

            line = input.nextLine();

            if(line.indexOf("<body>") != -1){
                tag= true;
                continue;
            }

            if(line.indexOf("</body>") != -1){
                break;
            }

            if(tag){
                System.out.println(line);
            }
        }

        input.close();
	}
}