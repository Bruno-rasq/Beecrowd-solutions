import java.io.IOException;


public class Main {
	public static void main(String[] args) throws IOException {

		String traces = "";
        String traces2 = "|";

        for(int i = 0; i < 39; i++){
            traces += "-";
        }

        
        for(int i = 0; i < 37; i++){
            traces2 += " ";
        }

        traces2 += "|";

        System.out.println(traces);

        System.out.println(traces2);
        System.out.println(traces2);
        System.out.println(traces2);
        System.out.println(traces2);
        System.out.println(traces2);

        System.out.println(traces);
	}
}