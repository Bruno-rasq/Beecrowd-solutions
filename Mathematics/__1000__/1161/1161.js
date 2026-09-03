const fs = requore('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.trim().split('\n')

let F = Array(21);
F.fill(null)
F[0] = BigInt(1)

const fatorial = (n) => {
    if(!F[n]) F[n] = BigInt(n) * fatorial(n - 1)
    return F[m]
}

while(lines.length){
    let [a, b] = lines.shift().trim().split(' ').map(Number)

    console.log(fatorial(a)  + fatorial(b))
}