const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").split("\n")
const notas = input.shift().split(' ').map(Number);
const exameNota = input.shift()
let [ a, b, c, d ] = notas;


function media(n: number, n2: number, n3: number, n4: number): number {
    let media = (((n * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10).toFixed(1);
    return parseFloat(media);
};

function media2(media: number, extra: number): number {
    let NovaM = (Number(media) + Number(extra)) / 2;
    return parseFloat(NovaM.toFixed(1))
};

function main() {

    let Media = media(a, b, c, d);
    let Media2 = media2(Media, Number(exameNota));

    console.log(`Media: ${Media}`);

    if(Media >= 7.0){
        console.log("Aluno aprovado.")
    
    } else if (Media < 5.0){
        console.log("Aluno reprovado.")
        
    } else if (Media >= 5.0 && Media <= 6.9){
        console.log("Aluno em exame.");
        console.log(`Nota do exame: ${exameNota}`)
    
        if(Media2 > 5){
            console.log("Aluno aprovado.")
    
        } else {
            console.log("Aluno reprovado.")
        }
        
        console.log(`Media final: ${Media2}`)
    
    };
};

main()