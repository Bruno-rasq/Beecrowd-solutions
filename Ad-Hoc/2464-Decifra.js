console.log(" 2464 - decifra ");

const input = `iohmunlcawygdfbqpvxzerjskt
haufhaimihbdqezihib`;

let lines = input.split('\n');
let key = lines[0].split('');
let enigma = lines[1].split('');

const Map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

let resp = '';

for (n in enigma){
    let indice = key.indexOf(enigma[n]);
    resp += `${Map[indice]}`
}

console.log(resp);