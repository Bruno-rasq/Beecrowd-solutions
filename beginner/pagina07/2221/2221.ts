const input_2221 = `3
5
12 23 15
42 12 20
2
52 1 11
1 52 1
3
95 12 22
5 51 21`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_2221 = input_2221.split('\n')

type Player = {
  dano: number,
  defesa: number,
  nivel: number
}

const cases = Number(lines_2221.shift())

const next = () => String(lines_2221.shift())

const statusPlayer = (input: string): Player => {
  let [dano, defesa, nivel] = input.split(' ').map(Number)
  return {dano, defesa, nivel}
} 

const battle = (dabriel: number, guarte: number) => {
  let response = ''
  if (dabriel > guarte) response = 'Dabriel'
  if (dabriel < guarte) response = 'Guarte'
  if (dabriel == guarte) response = 'Empate'
  return response 
}

for(let i = 0; i < cases; i++){
  let bonus   = Number(next())
  let dabriel = statusPlayer(next())
  let guarte  = statusPlayer(next())

  let valorD = (dabriel.dano + dabriel.defesa) / 2
  let valorG = (guarte.dano + guarte.defesa) / 2

  //atribuindo o bonus 
  guarte.nivel % 2 == 0 ? valorG += bonus : valorG
  dabriel.nivel % 2 == 0 ? valorD += bonus : valorD

  console.log(battle(valorD, valorG))
}