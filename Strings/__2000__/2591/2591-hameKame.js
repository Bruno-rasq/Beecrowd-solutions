console.log(" 2591 - hamekame ");

const input = `5
hamekame
haaamekaame
haaaamekaaame
haamekaaaame
hamekaaaaame`;

let lines = input.split('\n');
let int = Number(lines.shift());

for(let i = 0; i < int; i++){

    let data = lines[i].split('k');

    let data1 = data[0].split('');
    let data2 = data[1].split('');

    let cont1 = 0;
    let cont2 = 0;
    let A = 'a';

    for ( n in data1){
        if(data1[n] == A){
            cont1++
        }
    }
    for ( n in data2){
        if(data2[n] == A){
            cont2++
        }
    }

    let repeat = (cont1 * cont2);
    let response = 'k';
    response += 'a'.repeat(repeat)
    
    console.log(response)
};