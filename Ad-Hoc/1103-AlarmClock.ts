const input = `1 5 3 5
23 59 0 34
21 33 21 10
0 0 0 0`;

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const AlarmClock = (n1: number, n2: number, n3: number, n4:number): void => {

    let [h1, m1, h2, m2] = [n1, n2, n3, n4];
    
    if(h2 < h1 || (h2 == h1 && m2 < m1)) h2 += 24
    let time = (60 * h2 + m2) - (60 * h1 + m1)

    console.log(time)
}

const Setup = (datas: string[]): void => {

    for(let i = 0; i < datas.length; i++){
        let [h1, m1, h2, m2] = datas[i]
                    .split(' ')
                    .map(element => Number(element))

        if(h1 == 0 && h2 == 0 && m1 == 0 && m2 == 0) break

        else AlarmClock(h1, m1, h2, m2)
    }
}

Setup(lines)