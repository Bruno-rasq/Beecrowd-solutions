console.log(" 2958 - The bad vibes walk");

const input = `3 3
7V 1D 2D
2D 1V 1V
3V 5V 9D`

let lines = input.split('\n');
let [lin, col] = lines.shift().split(' ');
lin = Number(lin);
col = Number(col);

for (let i = 0; i < lin; i++) {

    let row = lines[i].split(' ');
    console.log(row)


    for (let n = 0; n < col; n++){
        let col = row[n]
        console.log(col)
    }

}