const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

let tag = false;

for(let i = 0; i < lines.length; i++){

    let line = lines[i]
    if(line.includes("<body>")){
        tag = true
        continue

    } else if(line.includes("</body>")){
        tag = false
        break
    }

    if(tag){
        console.log(line)
    }
}