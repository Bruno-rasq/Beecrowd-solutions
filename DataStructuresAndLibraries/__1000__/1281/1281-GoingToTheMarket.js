console.log(" 1281 - Going to the Market ");

const input = `2
4
mamao 2.19
cebola 3.10
tomate 2.80
uva 2.73
3
mamao 2
tomate 1
uva 3
5
morango 6.70
repolho 1.12
brocolis 1.71
tomate 2.80
cebola 2.81
4
brocolis 2
tomate 1
cebola 1
morango 1`;

let lines = input.split('\n');
let int = Number(lines.shift());

let t = 0;
while(t < int){
    
    let MarketProducts = Number(lines.shift())
    let Market = []
    for(let i = 0; i < MarketProducts; i++){
        let [fruit, price] = lines.shift().split(' ')
        Market[fruit] = Number(price)
    }

    let response = 0
    let requiredProd = Number(lines.shift());
    for(let j = 0; j < requiredProd; j++){
        let [name, q] = lines.shift().split(' ')
        response += Number(q) * Market[name]
    }

    console.log(`R$ ${response.toFixed(2)}`)
    
    ++t
}