const input = `7
5
>.....v
.......
.......
.......
^.....<`;

let lines = input.split('\n');
let width = Number(lines.shift());
let height = Number(lines.shift());
let count = 0

for(let i = 0; i < height; i++){
    for(let j = 0; j < width; j++){
        if(lines[i][j] == '*'){
            count++
        }
    }
};

if(count > 0){
    console.log('*')
} else {
    console.log('!')
};