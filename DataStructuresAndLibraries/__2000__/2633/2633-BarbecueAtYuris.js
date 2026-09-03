console.log(" 2633 - Barbecue at Yuri’s ");

const input = `3
picanha 15
coracao 14
maminha 37
4
alcatra 17
linguica 13
asinha 5
pernil 23`;

let lines = input.split('\n');
let output = []

function main(arry){

    for(let i = 0; i < arry.length; i++){

        let int = Number(arry.shift());
        let group = []
    
        for(let j = 0; j < int; j++){
            let data = arry.shift().split(' ')
            group.push(
                {
                    name: data[0],
                    value: Number(data[1])
                }
            )
        }
    
        group.sort((a, b) => {
            if(a.value > b.value){
                return - 1
            } else {
                return true
            }
        }).reverse();

        let resp = []
        group.forEach(obj => resp.push(obj.name))
        output.push(
            resp.join(' ')
        )
    }
}

main(lines)
console.log(output.join('\n'))