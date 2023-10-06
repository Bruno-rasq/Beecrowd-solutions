console.log(" 1234 - Dancing Sentence ");

const input = `This is a dancing sentence
  This   is         a  dancing   sentence  
aaaaaaaaaaa
z
 `;

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