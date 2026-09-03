import java.util.*;

public class Main {

    static Map<Integer, List<Integer>> grafo;
    static Set<Integer> visitados;

    public static void dfs(int node) {
        visitados.add(node);
        if (!grafo.containsKey(node)) return;

        for (int vizinho : grafo.get(node)) {
            if (!visitados.contains(vizinho)) {
                dfs(vizinho);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String linha = scanner.nextLine().trim();
            if (linha.isEmpty()) continue;

            String[] entrada = linha.split(" ");
            int leds = Integer.parseInt(entrada[0]);
            int segmentos = Integer.parseInt(entrada[1]);

            grafo = new HashMap<>();
            visitados = new HashSet<>();

            for (int i = 0; i < segmentos; i++) {
                String[] conexao = scanner.nextLine().trim().split(" ");
                int a = Integer.parseInt(conexao[0]);
                int b = Integer.parseInt(conexao[1]);

                grafo.putIfAbsent(a, new ArrayList<>());
                grafo.putIfAbsent(b, new ArrayList<>());
                grafo.get(a).add(b);
                grafo.get(b).add(a);
            }

            dfs(1);

            System.out.println(visitados.size() == leds ? "COMPLETO" : "INCOMPLETO");
        }

        scanner.close();
    }
}
