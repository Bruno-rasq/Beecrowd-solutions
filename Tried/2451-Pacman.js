console.log(" 2451 - Pacman ");

const input = `3
.....o.o.o....o.....oooo.oo.o.
.oo.oo.o.oooo.ooo.oo.o.....ooo
oo.oo..ooA...ooo.o..oooooo.o.o`;

let lines = input.split('\n');

let int = Number(lines.shift());

let safe = lines.filter(item => {
    return !item.includes('A')
});

let meal = 0;

for(let i = 0; i < safe.length; i++){
    let data = safe[i].split('');

    for (n in data){
        if(data[n] == 'o'){
            meal++
        }
    }

};

console.log(meal);