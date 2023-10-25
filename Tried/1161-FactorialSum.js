console.log(" 1161 - Factorial sum ");

const input = `4 4
0 0
0 2`;

let lines = input.split('\n')

for(let i = 0; i < lines.length; i++){

    let [ n1, n2 ] = lines[i].split(' ').map(el => Number(el))
    if(n1 === 0) n1 = 1
    if(n2 === 0) n2 = 1

    let fac = 1, fac2 = 1

    while(n1 >= 1){
        fac*= n1
        n1--
    }

    while(n2 >= 1){
        fac2*=n2
        n2--
    }

    console.log(fac + fac2)
}