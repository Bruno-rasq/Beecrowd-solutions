console.log(" 1120 - Contract Revision");

const input = `5 5000000
3 123456
9 23454324543423
9 99999999991999999
7 777
0 0`;

let lines = input.split('\n');
let response = []

for(let i = 0; i < lines.length; i++){

    let data = lines[i].split(' ')
    let [ A, B ] = data

    let revision = Revision(A, B)
    response[i] = revision
}

function Revision(str, str2){

    let arr = str2.split('');
    let aux = []

    for ( n in arr){
        if(arr[n] != str || arr[n] == '0'){
            aux[n] = arr[n] 
        }
    }

    if(aux.length == 0){
        return null

    } else if(aux.every(el => el == '0')){
        return '0'

    } else {
        return aux.join('')
    }
};

let resp = response.filter(item => {
    return item != null
});

resp.forEach(item => console.log(item));