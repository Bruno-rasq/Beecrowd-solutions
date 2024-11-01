import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(system.in);
        int n = in.nextInt();
        in.nextInt();

        ArrayList<String> villains = new ArrayList<>();

        for(int i = 0; i < n; i++){
            String villain = in.nextLine();
            boolean found = villains.contains(villain);

            if(!found){
                villains.add(villain);
                system.out.println("Y");
            } else {
                system.out.println("N");

            }
        }

        in.close();
    }
}