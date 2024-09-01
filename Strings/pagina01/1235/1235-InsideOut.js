console.log(" 1235 - Inside Out ");

const input = `5
I ENIL SIHTHSIREBBIG S
LEVELKAYAK
H YPPAHSYADILO
ABCDEFGHIJKLMNOPQRSTUVWXYZ
VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE`;

let lines = input.split("\n");

function ThisIsMyPlace(input){

    let integer = Number(input.shift())

    for(let i = 0; i< integer; i++){
        let data = input[i]
        let size = data.length / 2
        let ini = data.slice(0, size).split('').reverse().join('')
        let last = data.slice(size, data.length).split('').reverse().join('')
        let resp = `${ini}${last}`

        console.log(resp)
    }
};

ThisIsMyPlace(lines)