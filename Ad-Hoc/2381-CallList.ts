const input = `5 1
maria
joao
carlos
vanessa
jose`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n');


const  callList = (data : string[]): void  => {

    let [ props, ...list] = data
    let [n, p] = props.split(' ')

    const sortedList = list
                        .slice(0, +n)
                        .sort((a, b) => a.localeCompare(b))

    console.log(sortedList[+p - 1])
}

callList(lines)