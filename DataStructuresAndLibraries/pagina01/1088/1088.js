const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n")
const jogadores = ["Marcelo", "Carlos"]

const qnt_inversoes_necessarias = (arrOriginal) => {
    const arr = arrOriginal.slice() // evitar modificar o original

    const merge_sort_contador = (arr, inicio, fim) => {
        if (fim - inicio <= 1) return 0

        const meio = Math.floor((inicio + fim) / 2)
        const inv_esq = merge_sort_contador(arr, inicio, meio)
        const inv_dir = merge_sort_contador(arr, meio, fim)
        const inv_merge = merge_e_conta_inversoes(arr, inicio, meio, fim)

        return inv_esq + inv_dir + inv_merge
    }

    const merge_e_conta_inversoes = (arr, inicio, meio, fim) => {
        const temp = []
        let i = inicio, j = meio
        let inversoes = 0

        while (i < meio && j < fim) {
            if (arr[i] <= arr[j]) {
                temp.push(arr[i])
                i++
            } else {
                temp.push(arr[j])
                j++
                inversoes += meio - i
            }
        }

        while (i < meio) {
            temp.push(arr[i++])
        }
        while (j < fim) {
            temp.push(arr[j++])
        }

        for (let k = 0; k < temp.length; k++) {
            arr[inicio + k] = temp[k]
        }

        return inversoes
    }

    return merge_sort_contador(arr, 0, arr.length)
}

for (const linha of inputs) {
    const input = linha.trim().split(" ").map(Number)
    if (input.length === 1 && input[0] === 0) break

    const [n, ...permutacao] = input
    const inversoes = qnt_inversoes_necessarias(permutacao)
    const perdedor = jogadores[(inversoes + 1) % 2]
    console.log(perdedor)
}