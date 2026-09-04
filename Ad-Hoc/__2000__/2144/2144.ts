const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const repeticoes_maximas = (peso, reps) => peso * (1 + (reps / 30))

let medias: number[] = []
while (true) {
    const [w1, w2, reps] = input.shift().split(" ").map(Number)
    if (w1 === 0 && w2 === 0 && reps === 0) break;

    const w1_max = repeticoes_maximas(w1, reps);
    const w2_max = repeticoes_maximas(w2, reps);
    const media_rm = (w1_max + w2_max) / 2;
    medias.push(media_rm);

    if (1 <= media_rm && media_rm < 13) {
        console.log("Nao vai da nao")
    } else if (13 <= media_rm && media_rm < 14) {
        console.log("E 13")
    } else if (14 <= media_rm && media_rm < 40) {
        console.log("Bora, hora do show! BIIR!")
    } else if (40 <= media_rm && media_rm <= 60) {
        console.log("Ta saindo da jaula o monstro!")
    } else {
        console.log("AQUI E BODYBUILDER!!")
    }
}

let media_geral = medias.reduce((acc, val) => acc + val, 0) / medias.length;

if (media_geral > 40) {
    console.log("")
    console.log("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")
}
