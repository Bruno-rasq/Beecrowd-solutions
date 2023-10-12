console.log(" 1340 - I Can Guess the Data Structure! ");

const input = `6
1 1
1 2
1 3
2 1
2 2
2 3
4
1 2
1 1
2 1
2 2
2
1 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4`;

let lines = input.split('\n');
let output = []

for(let i = 0; i < lines.length; i++){

    let int = lines.shift();

    let inputData = [] // entrada de dados
    let outputData = [] // saida de dados

    for(let j = 0; j < int; j++){

        let data = lines.shift().split(' ').map(item => Number(item))
        
        if(data[0] == 1){
            inputData[j] = data[1]
        } else if(data[0] == 2){
            outputData[j] = data[1]
        }
    }

    let out = outputData.filter(item => item != null) // filtrando valores nulos

    
    // verificações
    let resp = ''
    let queue = VerificationQueue(inputData, out)
    let stack = VerificationStack(inputData, out)
    let Impos = VerificationImpossible(inputData, out)
    

    if(queue == true){
        resp = 'queue'
    }

    if(stack == true){
        resp = 'stack'
    }

    if(Impos == false){
        resp = 'impossible'
    }

    if(prioQueue == true && stack == false){
        resp = 'priority queue'
    }


    output.push(resp)

}

console.log(output.join('\n'))




function VerificationQueue(a1, a2){

    if(a1.length === a2.length && a1.every((value, index) => value === a2[index])){
        return  true
    } else {
        return false 
    };

}

function VerificationStack(a1, a2){

    let a1Reverse = [...a1].reverse()

    if(a1Reverse.length === a2.length && a1Reverse.every((value, index) => value === a2[index])){
        return  true
    } else {
        return false 
    };
}

function VerificationImpossible(a1, a2){

    return a1.some(el => a2.includes(el))
}


/*
    problema em verificar priority queue

    A1[1, 2, 3] e A2[3, 2, 1] = stack
    A1[1, 2, 3] e A2[1, 2, 3] = queue
    A1[1, 2, 3] e A2[5, 4, 8] = impossible
    A1[5, 2, 3, 1] e A2[5, 3] = ipriority queue

    !stack && !queue && !priorityqueue = not sure

*/