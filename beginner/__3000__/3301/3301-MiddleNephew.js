console.log(" 3301 - Middle Nephew ");

const input = `5 6 7`;

let lines = input.split(' ').map(el => Number(el))

let middle = lines.find(el => {
    let higher = Math.max(...lines)
    let less = Math.min(...lines)

    if(el != higher && el != less) return el
});

let resp = lines.indexOf(middle)

if(resp === 0){
    console.log('huguinho')

} else if(resp === 1){
    console.log('zezinho')

} else if(resp === 2){
    console.log('luisinho')
}