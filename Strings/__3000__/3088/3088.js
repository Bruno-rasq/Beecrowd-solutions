const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")

const fixText = (text) => {
    let fixed = ""
    for(let i = 0; i < text.length; i++){
        const char = text[i];
        const next = text[i + 1];
        if(char === " " && (next === "." || next === ",")){
            continue;
        }
        fixed += char;
    }
    return fixed;
}

console.log(input.map(fixText).join("\n"))