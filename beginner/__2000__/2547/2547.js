const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

let caso;
while (caso = input.shift()) {

    const [participantes, altura_minima, altura_maxima] = caso.split(" ").map(Number)

    let total_participantes_habeis = 0
    for(let i = 0; i < participantes; i++){
        const altura = Number(input.shift())
        if ( altura <= altura_maxima && altura >= altura_minima){
            total_participantes_habeis++
        }
    }

    console.log(total_participantes_habeis)
}