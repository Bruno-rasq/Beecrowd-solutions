const input = Number(require("fs").readFileSync("/dev/stdin", "utf8"))

const book_pages = (n) => {
    let total = 0
    const casas = [1_000_000, 100_000, 10_000, 1_000, 100, 10, 1]

    for(const casa of casas){
        if(n >= casa){
            let qnt = n - casa + 1
            let digitos = String(casa).length
            total += qnt * digitos
            n = casa - 1
        }
    }
    return total
}

console.log(book_pages(input))