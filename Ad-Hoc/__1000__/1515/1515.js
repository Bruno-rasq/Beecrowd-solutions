"use strict";
const input = require('fs').readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n');
const hello_galaxy = (galaxy) => {
    let planet = '';
    let curr = 5000;
    for (let i = 0; i < galaxy.length; i++) {
        let [name, age, valor] = galaxy[i].split(' ');
        let calc = Number(age) - Number(valor);
        if (calc < curr) {
            curr = calc;
            planet = name;
        }
    }
    console.log(planet);
};
const main = (arr) => {
    let I = true;
    while (I === true) {
        let int = Number(arr.shift());
        if (int === 0) {
            I = false;
        }
        else {
            let subgroup = [];
            for (let i = 0; i < int; i++) {
                let curr = String(arr.shift());
                subgroup.push(curr);
            }
            hello_galaxy(subgroup);
        }
    }
};
main(lines);
