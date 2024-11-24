const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8")
const lines = input.split('\n')

for(let i = -0; i < lines.length; i++){
    let line = lines[i].aplit('')
    let decrypt = ""

    for(let j = 0; j < line.length; j++){
        if (line[j] == "@"){decrypt += 'a'}
        else if (line[j] == "&"){decrypt += 'e'}
        else if (line[j] == "!"){decrypt += 'i'}
        else if (line[j] == "*"){decrypt += 'o'}
        else if (line[j] == "#"){decrypt += 'u'}
        else {decrypt += line[j]}
    }

    console.log(decrypt)
}