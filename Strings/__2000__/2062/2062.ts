const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split('\n')

const n_words: number = Number(input.shift())
const words: string[] = input.shift().split(' ')

let correct_words: string[] = []

for(let i = 0; i < n_words; i++){
    let word = words[i]
    if(word.length === 3){
        if(word.startsWith("OB")){
            correct_words.push('OBI')
        }
        else if(word.startsWith("UR")){
            correct_words.push('URI')
        }
        else {
            correct_words.push(word)
        }
    } else {
        correct_words.push(word)
    }
}

console.log(correct_words.join(' ').trim())