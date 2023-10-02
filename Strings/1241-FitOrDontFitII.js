console.log(" 1241 - Fit or Dont Fit II ");

const input = `4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554`;

let lines = input.split('\n');
let int = Number(lines.shift());

for(let i = 0; i < int; i++){

    let data = lines[i].split(' ')
    let [ A, B ] = data

    let response = FitOrDontFit( A, B )
    console.log(response)
};

function FitOrDontFit(str, str2){

    if( str2.length > str.length ){
        return 'nao encaixa';
    } else {

        let A = str.split('').reverse()
        let B = str2.split('').reverse()
        let arr = []

        for ( n in B ){
            if (B[n] == A[n]){
                arr[n] = 'V'
            } else {
                arr[n] = 'F'
            }
        }

        if(arr.includes('F')){
            return 'nao encaixa'
        } else {
            return 'encaixa'
        }
    }

};