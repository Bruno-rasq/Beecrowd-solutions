import * as fs from "fs"
const input: number = Number(fs.readFileSync("/dev/stdin", "utf8").trim())

const trailling_zeros = (n: number): number => {
    let count = 0;
    while (n >= 5) {
        n = Math.floor(n / 5)
        count += n
    }
    return count
}

console.log(trailling_zeros(input))