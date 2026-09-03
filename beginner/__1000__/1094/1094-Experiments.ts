const input = `10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

interface list {
    coelhos: number,
    ratos: number,
    sapos: number
}

namespace ALG {

    export const experiments = (obj: list): void => {

        let total = obj.coelhos + obj.ratos + obj.sapos

        const templete_response = [`Total: ${total} cobaias`,
                                    `Total de coelhos: ${obj.coelhos}`,
                                    `Total de ratos: ${obj.ratos}`,
                                    `Total de sapos: ${obj.sapos}`,
                                    `Percentual de coelhos: ${((100 * obj.coelhos) / total).toFixed(2)} %`,
                                    `Percentual de ratos: ${((100 * obj.ratos) / total).toFixed(2)} %`,
                                    `Percentual de sapos: ${((100 * obj.sapos) / total).toFixed(2)} %`];

        templete_response.forEach(element => console.log(element))
    }
}

namespace SETUP {

    export const trigger = (data: string[]): void => {

        let int = Number(data.shift())

        let infos: list = {
            coelhos: 0,
            ratos: 0,
            sapos: 0
        }

        for(let i = 0; i < int; i++){

            let [qnt, esp] = data[i]
                            .toString()
                            .split(' ')

            if(esp === 'C') infos.coelhos += Number(qnt)
            if(esp === 'R') infos.ratos += Number(qnt)
            if(esp === 'S') infos.sapos += Number(qnt)

        }
            
        ALG.experiments(infos)
    }
}

SETUP.trigger(lines)