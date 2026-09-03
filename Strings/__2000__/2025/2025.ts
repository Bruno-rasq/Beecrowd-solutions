const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n")
const n = Number(input.shift())

function corrigir_palavra(palavra) {
    if (palavra.length === 10 && palavra.slice(1, 9) === "oulupukk") {
        return "Joulupukki";
    } else if (palavra.length === 11 && palavra.slice(1, 9) === "oulupukk" && palavra.endsWith(".")) {
        return "Joulupukki.";
    }
    return palavra;
}

for(let i = 0; i < n; i++){
    const mensagem = input[i].split(" ")
    const corrigida = mensagem.map(palavra => corrigir_palavra(palavra))
    console.log(corrigida.join(" "))
}