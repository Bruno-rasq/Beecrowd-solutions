const input = `3 2
1
2 3
1
3 1
2`

// const input = require('fs').readFileSync('/dev/stdin', 'utf-8');
const lines = input.split('\n')

const OUTPUT = (games: number, inter: number, gremio: number, draw: number): void => {

    console.log(`${games} grenais`)
    console.log(`Inter:${inter}`)
    console.log(`Gremio:${gremio}`)
    console.log(`Empates:${draw}`)
    console.log(inter === gremio ? 'Não houve vencedor' : 
    `${inter > gremio ? 'inter' : 'gremio'} venceu mais`)
}

function main(){

    let G_win = 0
    let I_win = 0
    let draw = 0
    let games = 0
    let stop: boolean = false

    while(!stop){

        console.log('Novo grenal (1-sim 2-nao)')

        let [inter, gremio] = String(lines.shift()).split(' ').map(Number)
        let request = Number(lines.shift())

        if(inter === gremio)  draw++ // incrementa os empates
        inter > gremio ? I_win++ : G_win++ // incrementa as partidas vencidas
        request === 1 ? stop = false : stop = true // verifica condição de parada
        games++
    }
    
    OUTPUT(games, I_win, G_win, draw)
}

main()