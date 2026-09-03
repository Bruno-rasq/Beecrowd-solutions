namespace ALG {

    export const Sequence_II = (): void => {

        let i = 1
        let j = 7

        while(i < 10){
            
            for(let n = 0; n < 3; n++){
                console.log(`I=${i} J=${j--}`)
            }

            i += 2
            j  = 7
        }
        
    }
}

ALG.Sequence_II()