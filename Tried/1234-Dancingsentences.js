console.log(" 1234 - Dancing Sentence ");

const input = `This is a dancing sentence
This   is         a  dancing   sentence  
aaaaaaaaaaa
z`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++){

    let data = lines[i].split(' ')
    let response = DancingSentences(data)


    console.log(response)

}

function DancingSentences(arr){

    let resp = ''

    for (n in arr){
        if(arr[n] != ' '){
            let word = arr[n].split('');
            let aux = 1

            let A = []
            let a = []
            let total = 0

            for(n in word){
                A.push(word.shift().toUpperCase())
                a.push(word.shift())
            }

            if(A > a){
                total = A.length
            } else {
                total = a.length
            }

            let DancingWord = ''

            for(let i = 0; i< total; i++){
                if(A[i]){
                    DancingWord += A[i]
                }

                if(a[i]){
                    DancingWord += a[i]
                }
            }

           resp += DancingWord + ' '


        } else if (arr[n] == ' '){
            resp += ' '
        }
    }

    return resp

};