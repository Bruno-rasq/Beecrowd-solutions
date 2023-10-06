console.log(" 2137 - The Library of Mr. Severino ");

const input = `3
1233
0015
0100
7
0752
1110
0001
6322
8000
6321
0000`;

let lines = input.split('\n');

function main () {

    const output = []

    for (let i = 0; i < lines.length;){

        let numBooks = Number.parseInt(lines[i], 10)
        let sortedBooksCodes = lines.slice(i + 1, (i += numBooks + 1)).sort()

        output.push(sortedBooksCodes)
    }

    output.forEach(i => i.forEach(el => console.log(el)))
}

main()