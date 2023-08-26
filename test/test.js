console.log("1023 - drought");

const input = 
[`3
3 22
2 11
3 39`,

`5
1 25
2 20
3 31
2 40
6 70`,

`2
1 1
3 2`,

`0`];

let lines = input.map(item => item.split('\n'));

for(let i = 0; i < lines.length; i++){
    let int = lines[i].shift();

    console.log(Number(int));
}





