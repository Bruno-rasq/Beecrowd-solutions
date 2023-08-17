/*
    Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

    Input
    The input file contains an integer N.

    Output
    Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

*/

function TimeConvert(n) {

    let hours = Math.floor(n / 3600);
    let minu = Math.floor((n - (hours * 3600)) / 60);
    let second = Math.floor(n % 60);

    console.log(`${hours.toFixed(0)}:${minu.toFixed(0)}:${second}`);

}

TimeConvert(556);
TimeConvert(1);
TimeConvert(140153);




let n = Number(lines[0]);

let hours = Math.floor(n / 3600);
let minu = Math.floor((n - (hours * 3600)) / 60);
let second = Math.floor(n % 60);

console.log(`${hours.toFixed(0)}:${minu.toFixed(0)}:${second}`);