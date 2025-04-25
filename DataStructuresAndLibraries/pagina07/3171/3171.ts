const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");

const DFS = (visitados: Set<number>, grafico: { [key: number]: number[]}, node): void => {
    visitados.add(node);
    for (const vizinho of grafico[node] || []) {
        if (!visitados.has(vizinho)) {
            DFS(visitados, grafico, vizinho);
        }
    }
};

while (input.length > 0) {
    const [n_leds, n_segmentos] = input.shift().split(" ").map(Number);

    if (isNaN(n_leds) || isNaN(n_segmentos)) break; // evita erro em entradas inválidas

    const grafico: {[key: number]: number[]} = {};
    const visitados: Set<number> = new Set();

    for (let i = 0; i < n_segmentos; i++) {
        const [N, M] = input.shift().split(" ").map(Number);

        if (!grafico[N]) grafico[N] = [];
        if (!grafico[M]) grafico[M] = [];

        grafico[N].push(M);
        grafico[M].push(N);
    }

    DFS(visitados, grafico, 1);

    console.log(visitados.size === n_leds ? "COMPLETO" : "INCOMPLETO");
}
