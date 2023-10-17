console.log(" 3467 - This is my place ");

const input = `xxL
Lxx
xlx
xxL
xxL`;
let lines = input.split('\n');

// testando 1...
function main(input){

    let output = []
    input.forEach(element => {
        if(element === 'xxL' || element === 'xxl'){
            output.push(
                `Esse eh o meu lugar`
            )

        } else {
            output.push(`Oi, Leonard`)
        }
    });

    console.log(output.join('\n'))
};

// main(lines)


//tentativa 2...
// lines.forEach(data => {

//     switch(data){
//         case 'xxL':
//             console.log(`Esse eh o meu lugar`);
//             break;
    
//         default:
//             console.log(`Oi, Leonard`);
//             break;
//     };
// })