const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");

while (input.length >= 2) {
    const alien_vowels = input.shift();
    const frase = input.shift().split(" ");
    let contador = 0;

    for (const palavra of frase) {
        for (const char of palavra) {
            if (alien_vowels.includes(char)) {
                contador++;
            }
        }
    }

    console.log(contador);
}
