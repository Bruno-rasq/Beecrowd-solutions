const input_1983 = `4
900775 9.4
999999 9.9
10022 9.7
441002 9.8`

// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1983 = input_1983.split('\n')

const numero_de_alunos = Number(lines_1983.shift())


type Aluno = {
  matricula: number, 
  nota: number
}

const alunos: Aluno[] = lines_1983.map(user => {
  let [matricula, nota] = user.split(' ').map(Number)
  return { matricula, nota }
})

const O_escolhido = (alunos: Aluno[], tam: number) => {
  let escolhido = { "matricula": 0, "nota": 0 }

  for(let i = 0; i < tam; i++){
    let curr = alunos[i]

    if(curr.nota >= 8.0){
      if(escolhido.nota < curr.nota){
        escolhido = curr
      }
    }
  }

  escolhido.nota == 0 ? console.log('Minimum note not reached') : console.log(escolhido.matricula)
  
}

O_escolhido(alunos, numero_de_alunos)