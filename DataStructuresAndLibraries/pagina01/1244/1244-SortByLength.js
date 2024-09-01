console.log(" 1244 - sort by length ");

const input = `4
Top Coder comp Wedn at midnight
one three five
I love Cpp
sj a sa df r e w f d s a v c x z sd fd`;

let lines = input.split('\n');
let int = Number(lines.shift());

for (let i = 0; i<int; i++){
    let data = lines[i].split(' ');
    let response = orderByLength(data);
    
    console.log(response)
    
};

function orderByLength(arry){

    let order = arry.sort( (a, b) => {
        if(a.length < b.length){
            return 1
        }

        if(a.length > b.length){
            return -1
        }
    })

    return order.join(' ')
};