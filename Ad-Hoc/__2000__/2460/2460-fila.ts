const input = `4
10 9 6 3
1
3`

//const input = require('fs').readFileSync("/dev/stdin", "utf8");
const lines = input.split('\n').map(line => {
    return line.split(' ').map(element => Number(element))
})


function main(): void {

    let queue_length = lines[0][0]
    let queue = lines[1].slice(0, queue_length)

    let n_of_dropouts = lines[2][0]
    let dropouts = lines[3].slice(0, n_of_dropouts)

    let response = queue.filter(item => !dropouts.includes(item))

    console.log(response. join(' '))

}

main();
