console.log(" 1073 - Even Square ");

const input = `6`;

let lines = input.split('\n');
let int = Number(lines.shift());

function main(num){

    let output = []

    while(num > 0){
        if(num % 2 == 0){
            let resp = num**2
            output.push(
                `${num}^2 = ${resp}`
            )
        }
        
        num-=2
    }

    output.reverse()
    console.log(output.join('\n'))
}

main(int);