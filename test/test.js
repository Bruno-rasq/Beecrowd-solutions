console.log(" 1022 - TDA rational ");

let input = `4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4`

let lines = input.split('\n');
let int = Number(lines.shift());

// ----

console.log(lines)

for(let i = 0; i < int; i++){
    
   let currentData = lines[i].split(/\s+/).join('');
   
   switch(currentData[3]){

        case '+':
            console.log("soma");
            console.log(currentData);
            break;

        case '-':
            console.log("subtr");
            console.log(currentData);
            break;

        case '*':
            console.log("multi");
            console.log(currentData);
            break;

        case '/':
            console.log("divis");
            console.log(currentData);
            break;

        default:
   };
};
