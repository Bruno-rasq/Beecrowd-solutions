console.log(" 2428 - Capital ");

const input = `1 2 3 4`;

let lines = input.split(' ').map(el => Number(el));

function main() {

    let sortedList = lines.sort((a, b) => a - b)
    let [ a1, a2, a3, a4 ] = sortedList;
    let response = (a1 * a4 == a2 * a3) ? "S" : "N";

    console.log(response)
}

main()