console.log(" 1215 - Andy's First Dictionary ");

const input = `Ex(*$a#.mpl.e:

    Adventures in Disneyland
    
    Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT."
    
    So they went home.`;

let lines = input.trim().split("\n")
let dictionary = new Set()

for(let i = 0; i < lines.length; i++){
    let line = lines[i].toLowerCase().split(/[\W\b\s_\d]+/gi);
    for(let n = 0; n < line.length; n++){
        if(line[n] !== ''){
            dictionary.add(line[n])
        }
    }
}

let output = [...dictionary].sort((a, b) => a.localeCompare(b)).join('\n')

console.log(output);