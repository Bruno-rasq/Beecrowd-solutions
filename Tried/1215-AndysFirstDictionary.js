// console.log(" 1215 - Andy's First Dictionary ");

// const input = `Ex(*$a#.mpl.e:

//     Adventures in Disneyland
    
//     Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT."
    
//     So they went home.`;

// let lines = input.trim().split('\n');
// let dictionary = []


// for(let i = 0; i < lines.length; i++){
//     let line = lines[i].replace(/[,!$#@*&%;:,"'().]/g, " ").trim().split(' ')
//     for(let n = 0; n < line.length; n++){
//         if(line[n] != ''){
//             dictionary.push(line[n])
//         }
//     }
// }
// let output = dictionary.sort((a, b) => a.localeCompare(b)).filter((este, i) => dictionary.indexOf(este) === i);

// console.log(output.join('\n'))


console.log(" 1215 - Andy's First Dictionary ");

const input = `Ex(*$a#.mpl.e:

    Adventures in Disneyland
    
    Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT."
    
    So they went home.`;

let lines = input.trim().split("\n")
let dictionary = []

for(let i = 0; i < lines.length; i++){
    let line = lines[i].toLowerCase().split(/[\W\b\s_\d]+/gi);
    for(let n = 0; n < line.length; n++){
        dictionary.push(line[n])
    }
}

console.log(dictionary.sort((a, b) => a.localeCompare(b)).filter((este, i) => dictionary.indexOf(este) === i).join('\n'))