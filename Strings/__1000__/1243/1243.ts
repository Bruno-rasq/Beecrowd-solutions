const datas = require("fs").readFileSync("/dev/stdin", "utf8");
const inputs = datas.split("\n");
inputs.pop()

const media_frase = (frase) => {
    let total_palavras = 0;
    let somatoria_palavras = 0;
    
    for (const palavra of frase) {
        const palavra_limpa = palavra.endsWith(".") ? palavra.slice(0, -1) : palavra;
        
        if (/^[A-Za-z]+$/.test(palavra_limpa)) {
            somatoria_palavras += palavra_limpa.length;
            total_palavras++;
        }
    }
    
    if (total_palavras === 0) return 0;
    return Math.floor(somatoria_palavras / total_palavras);
};

for (const line of inputs) {
    const media = media_frase(line.split(" "));
    console.log(media <= 3 ? 250 : (media <= 5 ? 500 : 1000));
}