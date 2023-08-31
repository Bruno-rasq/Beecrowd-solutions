console.log(" 1387 - OG ");

const input = `2 2
2 3
5 5
1 1
0 0`;

let lines = input.split('\n');

for ( let i = 0; i < lines.length; i++){

    let data = lines[i].split(' ');
    let [Hom, Mul] = data;
    Hom = Number(Hom);
    Mul = Number(Mul);

    let soma = Hom + Mul;

    if( soma == 0 ){
        break;
     } else {
         console.log(soma)
     }
};