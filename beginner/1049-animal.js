console.log(" 1049 - animal ");

const input = `vertebrado
mamifero
onivoro`;

let lines = input.split('\n');

let wordA = lines[0];
let wordB = lines[1];
let wordC = lines[2];


if(wordA == 'vertebrado'){
    if(wordB == 'ave'){
        if(wordC == 'carnivoro'){
            console.log('aguia')
        } else if(wordC == 'onivoro'){
            console.log('pomba')
        }

    } else if(wordB == 'mamifero'){
        if(wordC == 'onivoro'){
            console.log('homem')
        } else if(wordC == 'herbivoro'){
            console.log('vaca')
        }
    }

} else if (wordA == 'invertebrado') {
    if(wordB == 'inseto'){
        if(wordC == 'hematofago'){
            console.log('pulga')
        } else if(wordC == 'herbivoro'){
            console.log('lagarta')
        }

    } else if(wordB == 'anelideo'){
        if(wordC == 'hematofago'){
            console.log('sanguessuga')
        } else if(wordC == 'onivoro'){
            console.log('minhoca')
        }

    }

};