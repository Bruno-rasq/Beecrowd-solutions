const datas = require("fs").readFileSync("/dev/stdin", "utf8")
const inputs = datas.trim().split("\n")
const n = Number(inputs.shift())

const nokia_keyboard = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777", "s": "7777",
    "t": "8", "u": "88", "v": "888",
    "w": "9", "x": "99", "y": "999", "z": "9999",
    " ": "0"
}

for(let i = 0; i < n; i++){
    const mensagem = inputs[i]
    let resultado = ""
    let tecla_anterior = ""

    for(const char of mensagem){
        const is_upper = char !== char.toLowerCase()
        const tecla = nokia_keyboard[char.toLowerCase()]
        const tecla_atual = tecla[0]

        // conflito com a tecla anterior
        if(tecla_atual === tecla_anterior){
            if(!is_upper){
                resultado += "*"
            }
        }

        if(is_upper){
            resultado += "#"
        }

        resultado += tecla
        tecla_anterior = tecla_atual
    }

    console.log(resultado)
}