const Sum_float = (num: number) => {
    return Math.round((num + 0.2) * 100) / 100
}


function main(){

    let I = 0
    let J = 1

    while( I <= 2){

        for(let i = 1; i <= 3; i++){
            console.log(`I=${I} J=${J}`)
            J++
        }

        J = Sum_float(J - 3)
        I = Sum_float(I)
    }
}

main()