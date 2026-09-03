const input = `0 0
5 12`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.trim().split('\n')

/**
 * @description função que dado uma lista de valores retorna o dobro da distancia
 * @returns exibi no console o resultado
 */
function back_to_high_school_physic() : void {

    for (let i = 0; i < lines.length; i++) {
        let [velocity, time] = String(lines[i]).trim().split(' ').map((x) => parseInt(x));

        console.log(velocity * 2 * time === -0 ? 0 : velocity * 2 * time);
    }
}

back_to_high_school_physic()