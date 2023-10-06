console.log(" 1040 - average 3 ");

const input = `2.0 4.0 7.5 8.0
6.0`;

let lines = input.split('\n');
let notas = lines.shift().split(' ').map((item) => Number(item));
let [ a, b, c, d ] = notas;
let exameNota = lines.shift()


function media(n, n2, n3, n4){
    let media = (((n * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10).toFixed(1);
    return media
};

function media2(media, extra){
    let NovaM = (Number(media) + Number(extra)) / 2;
    return NovaM.toFixed(1)
};

function main() {

    let Media = media(a, b, c, d);
    let Media2 = media2(Media, Number(exameNota));

    if(Media >= 7.0){
        console.log(`Media: ${Media}`);
        console.log("Aluno aprovado.")
    
    } else if (Media < 5.0){
        console.log(`Media: ${Media}`);
        console.log("Aluno reprovado.")
        
    } else if (Media >= 5.0 && Media <= 6.9){
        console.log(`Media: ${Media}`);
        console.log("Aluno em exame.");
        console.log(`Nota do exame: ${exameNota}`)
    
        if(Media2 > 5){
            console.log("Aluno aprovado.")
            console.log(`Media final: ${Media2}`)
    
        } else {
            console.log("Aluno reprovado.")
            console.log(`Media final: ${Media2}`)
        }
    
    };
};

main()