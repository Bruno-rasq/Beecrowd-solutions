console.log(" 1258 - T-shirt ");

const input = `9
Maria Jose
branco P
Mangojata Mancuda
vermelho P
Cezar Torres Mo
branco P
Baka Lhau
vermelho P
JuJu Mentina
branco M
Amaro Dinha
vermelho P
Adabi Finho
branco G
Severina Rigudinha
branco G
Carlos Chade Losna
vermelho P
3
Maria Joao
branco P
Marcio Guess
vermelho P
Maria Jose
branco P
0`;

let lines = input.split('\n');
lines.pop();

class Tshirt {
    constructor(name, color, size){
        this.name = name
        this.color = color
        this.size = size
    }
}

const comp = (a, b) => {
    if(a.color === b.color){
        if(a.size === b.size){
            if(a.name < b.name) return -1;
            if(a.name > b.name) return 1;
            return 0
        }

        if(a.size > b.size)return -1
        return 1
    }
    if(a.color < b.color)return -1
    return 1
}

let first = true
while(lines.length){
    let int = Number(lines.shift())
 
    if(first){
        first = false
    } else {
        console.log('')
    }

    let camisetas = []
    for(let i = 0; i < int; i++){
        let name = lines.shift()
        let [color, size] = lines.shift().split(' ')

        camisetas.push(
            new Tshirt(name, color, size)
        )
    }

    camisetas.sort(comp)

    for(let i = 0; i < int; ++i){
        console.log(`${camisetas[i].color} ${camisetas[i].size} ${camisetas[i].name}`)
    }
}