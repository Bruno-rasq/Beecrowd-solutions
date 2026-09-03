const input = `4
7
44
0x80685
-1`

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')


function main() : void  {

    let curr: string = String(lines.shift())

    while(curr != '-1'){

        String(curr).includes('0x') 
        ? console.log(Number(curr)) 
        : console.log(`0x${Number(curr).toString(16).toUpperCase()}`)

        curr = String(lines.shift())
    }
    
}

main()