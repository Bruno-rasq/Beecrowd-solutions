/*
    Make a program that reads three floating point values: A, B and C. Then, calculate and show:
    a) the area of the rectangled triangle that has base A and height C.
    b) the area of the radius's circle C. (pi = 3.14159)
    c) the area of the trapezium which has A and B by base, and C by height.
    d) the area of ​​the square that has side B.
    e) the area of the rectangle that has sides A and B.

    Input
    The input file contains three double values with one digit after the decimal point.

    Output
    The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.

*/

let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);
let C = parseFloat(lines[2]);
let pi = parseFloat(3.14159);

let Triangle = ((A * C) / 2);
let raio = ((C ** 2) * pi);
let trapezium = (((A + B) * C) / 2);
let square = (B ** 2);
let rectangle = (A * B);

console.log(`TRIANGULO: ${Triangle.toFixed(3)}`);
console.log(`CIRCULO: ${raio.toFixed(3)}`);
console.log(`TRAPEZIO: ${trapezium.toFixed(3)}`);
console.log(`QUADRADO: ${square.toFixed(3)}`);
console.log(`RETANGULO: ${rectangle.toFixed(3)}`);
