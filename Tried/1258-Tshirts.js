console.log(" 1258 - T-shirt ");

const input = `9
Maria Jose
branco P
Mangojata Mancuda
vermelho P
Cezar Torres Mo
branco P
Baka Lhau
vermelho P
JuJu Mentina
branco M
Amaro Dinha
vermelho P
Adabi Finho
branco G
Severina Rigudinha
branco G
Carlos Chade Losna
vermelho P
3
Maria Joao
branco P
Marcio Guess
vermelho P
Maria Jose
branco P
0`;

let lines = input.split('\n');

function main(arry){

    let  output = []

    for(let i = 0; i < arry.length; i++){

        let int = Number(arry.shift())
        if(int == 0 || int == '0') break;

        let white = []
        let red = []

        for(let j = 0; j < int; j++){
            let name = arry.shift()
            let shirt = arry.shift().split(' ')

            if(shirt[0] == 'vermelho'){
                red.push(
                    {
                        color: shirt[0],
                        size: shirt[1],
                        name: name
                    }
                )
            }
            if(shirt[0] == 'branco'){
                white.push(
                    {
                        color: shirt[0],
                        size: shirt[1],
                        name: name
                    }
                )
            }
        }

        white.sort((shirtA, shirtB) => {
            if(shirtA.size !== shirtB.size){
                return shirtA.size.localeCompare(shirtB.size)
            }
        }).reverse();

        red.sort((shirtA, shirtB) => {
            if(shirtA.size !== shirtB.size){
                return shirtA.size.localeCompare(shirtB.size)
            }
        }).reverse();

        white.forEach(obj => {
            output.push(
                `${obj.color} ${obj.size} ${obj.name}`
            )
        })

        red.forEach(obj => {
            output.push(
                `${obj.color} ${obj.size} ${obj.name}`
            )
        })

    }
    
    console.log(output.join('\n'))
}

main(lines)