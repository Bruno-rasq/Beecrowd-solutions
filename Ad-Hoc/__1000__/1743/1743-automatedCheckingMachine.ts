const input = `1 1 0 1 0
0 0 1 0 1`;

//const input = require('fs').readFileSync('/dev/stdin', "utf8");
const lines = input.split('\n');


function Automated_chacking_machine(arr1: number[], arr2: number[]): void {

    let response: string = ''
    for(let i = 0; i < arr1.length; i++){

        if(arr1[i] === arr2[i]){
            response = 'N'
            break
        }
    }

    response === '' ? console.log('Y') : console.log('N')

} // O(1)

function main(): void {

    let plugs1 = String(lines.shift()).split(' ').map(element => Number(element))
    let plugs2 = String(lines.shift()).split(' ').map(element => Number(element))

    Automated_chacking_machine(plugs1, plugs2)
}

main()  