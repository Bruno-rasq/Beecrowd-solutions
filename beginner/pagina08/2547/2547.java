import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        try {
            while(in.hasNextLine()){

                String line = in.nextLine().trim();

                if(line.isEmpty()) continue;

                String[] data = line.split(" ");
                if(data.length < 3) break;
                int participantes = Integer.parseInt(data[0]);
                int altura_minima = Integer.parseInt(data[1]);
                int altura_maxima = Integer.parseInt(data[2]);
                int total_participantes_habeis = 0;

                in.nextLine();
                for(int i = 0; i < participantes; i++){
                    if(!in.hasNextLine()) break;
                    String alturaLine = in.nextLine().trim();
                    if(alturaLine.isEmpty()) continue;
                    int altuta = Integer.parseInt(alturaLine);

                    if(altura >= altura_minima && altura <= altura_maxima)
                        total_participantes_habeis++;
                }

                System.out.println(total_participantes_habeis);
            }
        }

        in.close();
    }
}