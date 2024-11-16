const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split(' ')
let [entrag, prazo ] = input.map(Number)

if (prazo - entraga >= 1){

    console.log("Muito bem!, Apresenta antes do Natal!")
}

else if (prazo - entraga < 0){

    console.log("Eu te odeio professora!")
}

else if (prazo - entraga < 3){

    console.log("Parece o trabalho do meu filho!")
    prazo += 2
    if (prazo <= 24){

        console.log("TCC Apresentado!")
    }
    else{

        console.log("Fail! Entao eh nataaaaal!")
    }
}