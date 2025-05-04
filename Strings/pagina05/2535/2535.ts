const inputs = require("fs").readFileSync("/dev/stdin", "utf8").split("\n")

const pet_valido = (inicial_raca, nome) => {
    for(const parte of nome){
        // parte[0] seria a inicial desta parte do nome
        if(parte[0] == inicial_raca) return true
    }

    return false
}

while(inputs.length > 0){

    const n_pets = Number(inputs.shift())
    const n_pets_validos = 0

    for(let i = 0; i < n_pets; i++){

        const especie = inputs.shift()
        const raca = inputs.shift()
        const nome = inputs.shift().split(" ")

        inputs.shift() // lê a linha vazia

        n_pets_validos += (especie == "cachorro" && nome.length > 1 && pet_valido(raca[0], nome)) ? 1 : 0  
    
    }
    console.log(n_pets_validos)
}