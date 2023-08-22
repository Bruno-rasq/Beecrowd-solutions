console.log(" 1022 - TDA rational ");

let input = `4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4`

let lines = input.split('\n');
let int = Number(lines.shift());

// ----

for(let i = 0; i < int; i++){
    
   let currentData = lines[i].split(/\s+/).join('');

   let n1 = Number(currentData[0]);
   let d1 = Number(currentData[2]);
   let n2 = Number(currentData[4]);
   let d2 = Number(currentData[6]);

   let response = "";
   
   switch(currentData[3]){

        case '+':
            response = ((n1 * d2) + (n2 * d1)) + "/" + ( d1 * d2);
            console.log(response);
            break;

        case '-':
            response = ((n1 * d2) - (n2 * d1)) + "/" + ( d1 * d2);
            console.log(response);
            break;

        case '*':
            response = (n1 * n2) + "/" + ( d1 * d2);
            console.log(response);
            break;

        case '/':
            response = (n1 * d2) + "/" + (n2 * d1);
            console.log(response);
            break;

        default:
   };
};
