const input_3357 = `3 3.5 0.3
Maria Juca Bob`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_3357 = input_3357.split('\n')

const current_data = () => String(lines_3357.shift())
const to_list = (data: string) => data.split(' ')

function ListaCircular(list: string[]) {
  let nomes = list
  let index = 0 
  return () => {
    let nome = nomes[index]
    index = (index + 1) % nomes.length
    return nome
  }
}

let [p, litros, cabaca ] = to_list(current_data()).map(Number)
const nomes = to_list(current_data())

const lista_circular = ListaCircular(nomes) 

let rico = ''
while (litros >= cabaca){
  litros -= cabaca
  rico = lista_circular()
}

rico = lista_circular()

console.log(`${rico} ${litros.toFixed(1)}`)