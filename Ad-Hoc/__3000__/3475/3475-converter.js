console.log(" 3475 - converter ");

const input = `2
tres
4
seis
0
quatro
oito`;

let lines = input.split("\n");

function Converter(input){

    for(let i = 0; i < input.length - 1; i++){
        let nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

        let numsString = ['zero', 'um', 'dois', 'tres', 'quatro', 
                        'cinco', 'seis', 'sete', 'oito', 'nove'];

        let index = nums.indexOf(input[i])
        let index2 = numsString.indexOf(input[i])

        if(index === -1){
            console.log(nums[index2])
        } else if(index2 === -1){
            console.log(numsString[index])
        }
    }
}

Converter(lines)