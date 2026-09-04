console.log(" 1546 - feedBack ");

const input = `2
4
1
1
3
4
3
3
3
2`;

let lines = input.split('\n');
let int = Number(lines.shift());
let output = []

/*
   1 Compliments: Rolien
   2 Bugs: Naej
   3 Questions: Elehcim
   4 Suggestions: Odranoel

*/

for(let i = 0; i < int; i++){

    let days = lines.shift()
    let response = []

    for(let j = 0; j < days; j++){
        let responsible = Number(lines.shift());

        if(responsible == 1){
            response[j] = 'Rolien'
        }
        if(responsible == 2){
            response[j] = 'Naej'
        }
        if(responsible == 3){
            response[j] = 'Elehcim'
        }
        if(responsible == 4){
            response[j] = 'Odranoel'
        }
    }

    output.push(
        response.join('\n')
    )
}

console.log(output.join('\n'))