import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").split(' ').map(Number)

const get_middle_element_index = (list: number[]): number {

    let max = Math.max(...list);
    let min = Math.min(...list);

    for(let i = 0; i < 3; i++){
        if(list[i] != min && list[i] != max) return i;
    }
    return -1;
}

const sobrinhos: string[] = ["huguinho", "zezinho", "luisinho"];

console.log(sobrinhos[get_middle_element_index(input)]);