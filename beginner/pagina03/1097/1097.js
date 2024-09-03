const sequenceij3 = () => {
    let i = 1;
    let j = 7;

    while(i < 10){
        for(let interador = 0; interador < 3; interador++){
            console.log(`I=${i} J=${j}`)
            j--
        }
        i += 2
        j += 5
    }
}

sequenceij3()