const input = `2
127 255 255 255 255
128 255 255 255 255
0`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines: string[] = input.split('\n')

function setup (list: string[]): string[] {

    let arr: string[] = []
    while(list.length){
        let qst = Number(list.shift())

        if(!qst) break //EOF
        
        for(let n = 0; n < qst; n++){
            let data = list.shift()
            arr.push(`${data}`)
        }
    }

    return arr
} 

function readAlternatives(list: string[]):void {
    list.forEach(QA => {
        let data = QA.split(' ').map(element => Number(element))
        OUTPUT(data)
    })
}

function dubleAlternative(arr: string[]): boolean {
    let DA = 0;
    for(let n = 0; n < arr.length; n++){
        if(arr[n] == 'B') DA++
    }

    return DA == 1 ? false : true
}

function ABCED(n: number): string  {
    let Alt: string = '';
    if(n >= 0 && n <= 127) Alt = 'B'
        else if(n > 127 && n <= 255) Alt = 'W'
        else if(n > 255 || n < 0)  Alt = 'D'

    return Alt
}

function response(auxArr: string[]): string[] {
    let res: string[] = [];
    if(dubleAlternative(auxArr) || auxArr.includes('D') || auxArr.includes('B') == false){
        res.push('*')

    }else {
        let index = auxArr.indexOf('B') + 1;
        if(index == 1) res.push('A')
        if(index == 2) res.push('B')
        if(index == 3) res.push('C')
        if(index == 4) res.push('D')
        if(index == 5) res.push('E')
    }

    return res
}

function OUTPUT(list: number[]): void{

    let aux: string[] = []
    list.forEach((num) => {
        aux.push(ABCED(num))
    })

    response(aux).forEach(ALT => console.log(ALT))
}

const alternatives = setup(lines)
readAlternatives(alternatives)