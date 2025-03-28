const fs = require("fs")
const input = Number(fs.readFileSync("/dev/stdin", "utf8").trim())

const trailling_zeros = (n) => {
    let count = 0;
    while (n >= 5) {
        n = Math.floor(n / 5)
        count += n
    }
    return count
}

console.log(trailling_zeros(input))