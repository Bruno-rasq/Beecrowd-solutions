import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")

const fixText = (text: string): string => {
    let fixed: string = "";
    for(let i = 0; i < text.length; i++){
        const char: string = text[i];
        const next: string = text[i + 1];
        if(char === " " && (next === "." || next === ",")){
            continue;
        }
        fixed += char;
    }
    return fixed;
}

console.log(input.map(fixText).join("\n"))