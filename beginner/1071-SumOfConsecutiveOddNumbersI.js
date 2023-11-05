console.log(" 1071 - Sum of Consecutive Odd Numbers I ");

const input = `12
12`;

let lines = input.split('\n').map(el => Number(el));

let [n1, n2] = lines

if(n1 > n2){
    [n1, n2] = [n2, n1]
}

n1 += (Math.abs(n1) % 2) + 1 
n2 -= (Math.abs(n2) % 2) + 1

let soma = 0
for (let i = n1; i <= n2; i += 2) {
    soma += i;
}

console.log(soma)