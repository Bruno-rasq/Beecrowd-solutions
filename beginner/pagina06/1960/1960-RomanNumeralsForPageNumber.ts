const input = `999`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const Roman_numerals_for_page = (num: number): void => {
    
    const RomanNumberMap = {
        u: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], //Unidade
        d: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"], //Dezena
        c: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], //Centena
        m: ["M"] // Milhar
    };

    let str = String(num);
    let arry = Array.from(str).reverse();

    let uni = Number(arry[0]);
    let dez = Number(arry[1]);
    let cen = Number(arry[2]);
    let mil = Number(arry[3]);

    arry[0] = RomanNumberMap.u[uni - 1] ?? "";
    arry[1] = RomanNumberMap.d[dez - 1] ?? "";
    arry[2] = RomanNumberMap.c[cen - 1] ?? "";
    arry[3] = RomanNumberMap.m[mil - 1] ?? "";

    console.log(arry.reverse().join(''))

}

Roman_numerals_for_page(Number(lines.shift()))