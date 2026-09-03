console.log(" 2791 - bean");

const input = `0 0 0 1`;

let lines = input.split(' ');

let response = null;

for (let i = 0; i < lines.length; i++) {

    if ( Number(lines[i]) == 1 ) {
        response = i+1;
    }
};

console.log(response);
