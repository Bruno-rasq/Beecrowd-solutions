const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
let lines = input.split('\n');

for ( let i = 0; i < lines.length; i ++ ){
    let data = lines[i].trim().split('');

    let parenthese = data.filter(item => {
        return item == "(" || item == ")";
    });

    if(parenthese.length == 0){
        break

    } else {

        let countverifi = count(parenthese);
        let FirstAndLastVerif = FirtsAndLast(parenthese);

        if(countverifi == true && FirstAndLastVerif == true){
            console.log("correct")
        } else {
            console.log("incorrect")
        };
    }
 
}

function count(data: string[]): boolean {
    let count = 0

    for (let i = 0; i < data.length; i++){
        if(data[i] == "("){
            count++
        } else {
            count--
        }
    };

    if(count == 0){
        return true
    } else {
        return false
    }
};

function FirtsAndLast(data: string): boolean {

    let first = data[0];
    let last = data[data.length-1];

    if (first == ")" || last == "("){
        return false
    } else {
        return true
    }
};