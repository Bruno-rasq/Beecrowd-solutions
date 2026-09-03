const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const numero_casos = Number(inputs.shift())

inputs.pop()

const calcular_frequencia = (total, faltas) => {
    const presencas = total - faltas
    const frequencia = (presencas * 100) / total
    return frequencia >= 75
}

for(let i = 0; i < numero_casos; i++){
    const numero_alunos = Number(inputs.shift())
    const alunos = inputs.shift().split(" ")
    const frenqu = inputs.shift().split(" ")
    
    let alunos_baixa_frequencia = []
    
    for(let j = 0; j < numero_alunos; j++){
        const aluno = alunos[j]
        const frequencias = frenqu[j]
        
        let faltas = 0
        let total = 0
        
        for(const frequencia of frequencias){
            if (frequencia == "A") faltas += 1
            if (frequencia == "M") continue
            total += 1
        }
        
        if (!calcular_frequencia(total, faltas)) alunos_baixa_frequencia.push(aluno)
    }
    
    console.log(alunos_baixa_frequencia.length > 0 ? alunos_baixa_frequencia.join(" ") : "")
}