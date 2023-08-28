console.log(" 2006 - identiflyng tea")

const input = `1
1 2 3 2 1`;

let lines = input.split('\n');
let tea = lines.shift();

let teatest = lines[0].split(/\s+/);
let response = 0;

for(let i = 0; i < 5; i ++){

    if(teatest[i] == tea){
        response++
    }
}

console.log(response);