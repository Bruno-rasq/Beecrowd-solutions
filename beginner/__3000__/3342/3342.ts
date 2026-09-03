import * as fs from "fs"

const input = fs.readFIleSync("/dev/stdin", "utf8")

function keanuChess(input: number): void {
    
    let total_cases = input * input;
    let b = 0, p = 0

    if (input % 2 == 0){
        b = total_cases / 2;
        p = total_cases / 2;
    } else {
        b = (total_cases + 1) / 2;
        p = b - 1
    }
    console.log(`${b} casas brancas e ${p} casas pretas`)
}

keanuChess(Number(input))