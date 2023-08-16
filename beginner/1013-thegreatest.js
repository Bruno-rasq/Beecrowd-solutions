/*
    Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

    Input
    The input file contains 3 integer values.

    Output
    Print the greatest of these three values followed by a space and the message “eh o maior”.


*/

let [ a, b, c ] = lines[0].split(' ');
let arry = [];
arry.push(a, b, c);

let maior = Math.max(...arry);
console.log(`${maior} eh o maior`);