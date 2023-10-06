console.log(" 1041 - Coordinates of a Point ");

const input = `4.5 -2.2`;

let lines = input.split(' ').map(i => Number(i));
let [ a, b ] = lines


function main(){

    if(a == 0 && b == 0){
        console.log('Origem')

    } else if( a == 0 ){
        console.log('Eixo Y')
    } else if( b == 0){
        console.log('Eixo X')
        
    } else {
        let testA = a > 0 ? true : false;
        let testB = b > 0 ? true : false;

        if(testA == true && testB == true){
            console.log('Q1'); 

        } else if(testA == true && testB == false){
            console.log('Q4');

        } else if(testA == false && testB == true){
            console.log('Q2');

        } else if(testA == false && testB == false){

            console.log('Q3');
        }

    }
};

main()