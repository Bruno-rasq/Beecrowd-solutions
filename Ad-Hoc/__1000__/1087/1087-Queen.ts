const input = 
`4 4 6 2
3 5 3 5
5 5 4 3
0 0 0 0`

const lines = input.split('\n');
lines.pop();


const Main = (): void => {

    // pq de lines.length - 1 Nâo sei! só funciona assim
    while(lines.length - 1){

        let Line = `${lines.shift()}`
        let [ x1, y1, x2, y2 ] = Line.trim().split(' ').map(elem => +elem)

        if(x1 === x2 && y1 === y2){
            console.log(0)
        } else {

            if(x1 == x2 || y1 == y2 || Math.abs(x1 - x2) === Math.abs(y1 - y2)){
                console.log(1)
            } else {
                console.log(2)
            }
        }
    }
}

Main()