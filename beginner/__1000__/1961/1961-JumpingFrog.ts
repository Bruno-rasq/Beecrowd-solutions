const input = `5 10
1 3 6 9 7 2 4 5 8 3`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const setData = (data: string): number[] => data.split(' ').map(element => Number(element))
  
const Game = (data: string[]): void => {
    let [High_Jump, Number_of_PIPES] = setData(String(data.shift()))
    let Pipes = setData(String(data.shift()))

    let response = true
    for(let i = 0; i < Number_of_PIPES; i++){
        // se pilhar for maior que altura atual + altura do pulo
        // ou se pilhar for menor que altura atual - altura do pulo
        if(Math.abs(Pipes[i] - Pipes[i - 1]) > High_Jump){
            response = false
            break
        }
        
    }

    console.log(response ? 'YOU WIN' : 'GAME OVER')
}

Game(lines)