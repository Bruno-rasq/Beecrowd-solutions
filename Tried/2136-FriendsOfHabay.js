console.log(" 2136 - Friends of Habay ");

const input = `João NÃO
Carlos SIM
Abner NÃO
Samuel SIM
Ricardo NÃO
Abhay SIM
Samuel SIM
André SIM
Roberto NÃO
Carlos SIM
Samuel SIM
Samuel SIM
Abhay SIM
Aline SIM
André SIM
FIM`;

let lines = input.split('\n')
lines.pop()

let Sim = new Set()
let Nao = new Set()

while(lines.length){
    let req = lines.shift()
    
    let [name, voto] = req.split(' ')
    if(voto === 'SIM'){
        Sim.add(name)
    } else {
        Nao.add(name)
    }
}

let choose = [...Sim].sort((a, b) => {
    if(a.length > b.length){
        return -1
    } else {
        return 1
    }
})
let S = [...Sim].sort((a, b) => a.localeCompare(b))
let N = [...Nao].sort((a, b) => a.localeCompare(b))

let output = [...S, ...N]
output.push(
    '',
    'Amigo do Habay:',
    `${choose[0]}`

)

console.log(output.join('\n'))