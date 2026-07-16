const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
let p1 = 0;
let p2 = input.length - 1;
let isp = true;

while(p1 != p2){
    if(input[p1] != input[p2]){
        isp = false;
        break;
    }
    p1++;
    p2--;
}

let ans = `A frase [${input}]` + (isp ? "eh palidrome" : "nao eh palindrome");
console.log(ans);