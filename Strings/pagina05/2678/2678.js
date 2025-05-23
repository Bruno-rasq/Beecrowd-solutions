const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n")

const nokia_keyboard = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9",
}

for(const input of inputs){
    let output = ""
    
    for(const chr of input){
        if(/^[A-Za-z]+$/.test(chr)) output += nokia_keyboard[chr.toLowerCase()]
        if(["#", "*"].includes(chr) || /^\d+$/.test(chr)) output += chr
    }
    
    console.log(output)
}