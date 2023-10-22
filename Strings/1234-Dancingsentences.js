console.log(" 1234 - Dancing Sentence ");

const input = `This is a dancing sentence
  This   is         a  dancing   sentence  
aaaaaaaaaaa
z
 `;


let lines = input.trim().split('\n');

while(lines.length){
    let sentence = lines.shift()

    let maiuscula = true
    let response = sentence.split('').map((x) => {
        let letra = x

        if(/[A-Za-z]/.test(x)){
            if(maiuscula){
                letra = letra.toUpperCase();
            } else {
                letra = letra.toLowerCase();
            }
            maiuscula = !maiuscula
        }

        return letra
    }).join('')

    console.log(response)
}

/*
 ERRO: 
let lines = input.split('\n');
let output = []

for(n in lines){

    let data = lines[n].split('');

    if(data == null || data == ' ' || data == undefined) break;

    let response = ''
    let aux = 1
    
    for(i in data){

        if(data[i] != ' ' && aux == 1){
            response += data[i].toUpperCase()
            aux--

        } else if(data[i] != ' ' && aux == 0){
            response += data[i].toLowerCase()
            aux++

        } else if(data[i] === ' '){
            response += data[i]
        }
    }

    output[n] = response
};

console.log(output.join('\n'))
*/