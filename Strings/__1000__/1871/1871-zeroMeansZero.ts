// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')


const Main = (): void => {

    let arr = lines

    arr.pop() // EOF 

    arr.forEach((item: string) => {

        let [a, b] = item.trim().split(' ').map(el => +el)

        let sum = `${a + b}`
        let response = sum.replace(/[0]/g, "")

        console.log(response)
    })

    // while(lines.length){
    //     let [M, N] = lines.shift().trim().split(' ').map((x) => parseInt(x));

    //     if(!M && !N)    break;

    //     let soma = (M + N).toString();
    //     let resposta = soma.split('0').join('');

    //     console.log(resposta);
    // }
}

Main()