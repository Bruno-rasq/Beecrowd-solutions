const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n").pop()

const DFS = (visitados, grafico, node) => {
    visitados.add(node)
    for(const vizinho of grafico[node]){
        DFS(visitados, grafico, vizinho)
    }
}

while (input.length > 0){

    const [n_leds, n_segmentos] = input.shift().split(" ").map(Number)
    
    let grafico = {}
    let visitados = new Set()

    for(let i = 0; i < n_segmentos; i++){
        const [N, M] = input.shift().split(" ").map(Number)

        if(!Object.keys(grafico).includes(N)) grafico[n] = []
        if(!Object.keys(grafico).includes(M)) grafico[n] = []

        grafico[N].push(M)
        grafico[M].push(N)
    }

    DFS(visitados, grafico, 1)

    console.log(visitados.size() == n_leds ? "COMPLETO" : "INCOMPLETO")

}