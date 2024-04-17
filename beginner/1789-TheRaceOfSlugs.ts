const input = `10
10 10 10 10 15 18 20 15 11 10
10
1 5 2 9 5 5 8 4 4 3
10
19 9 1 4 5 8 6 11 9 7`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const setData = (data: string): number[] => data.split(' ').map(element => Number(element));

const Velocity_leval = (velocity: number): number => {
    if (velocity < 10) return 1
	else if (velocity >= 10 && velocity < 20) return 2
	else return 3
};
  
const Fast_slugs = (data: string[]): void => {
    
    for(let i = 0; i < data.length; i += 2){
        if(data[i] == '') break

        let int = Number(data[i])
        let slugs = setData(String(data[i + 1]))

        let Max = 0
        for(let j = 0; j < int; j++){
            if(slugs[j] > Max){
                Max = slugs[j]
            }
        }

        console.log(Velocity_leval(Max))
    }
}

Fast_slugs(lines)