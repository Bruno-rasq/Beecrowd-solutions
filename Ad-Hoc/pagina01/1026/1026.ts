import * as fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")

let arr = new Uint32Array(3);
for(const line of input){

    if(line != ''){
        let [a, b] = line.split(" ").map(Number);
        arr[0] = a;
        arr[1] = b;
        arr[2] = a ^ b;
        console.log(arr[2])
    }
}