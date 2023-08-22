//adiantando algumas partes

/*
    inpult format 

    number / number, operador( +, -, *, /) number / number
    n1/d1 operador( +, -, *, /)  n2/d2

*/

response = null;

switch(operrador){
    case '+':
        response = (((n1 * d2) + (n2 * d1)) / (d1 * d2));
        break;

    case '-':
        response = (((n1 * d2) - (n2 * d1)) / (d1 * d2));
        break;

    case '*':
        response = ((n1 * n2) / (d1 * d2));
        break;

    case '/':
        response = ((n1 * d2) / (n2 * d2));

}

/*
    resposta:

    console.log(`${response} = ${simplify}`);
    resposta da operação "=" simplificação da resposta ou caso não seja possivel a propria resposta

*/

function test(str){

    let split = str.split("+");

    let arry1 = split[0].split("/");
    let [ n1, d1 ] = arry1.map(item => parseFloat(item));

    let arry2 = split[1].split("/");
    let [ n2, d2 ] = arry2.map(item => parseFloat(item));

    console.log(str)
    console.log(n1, n2, d1, d2)
    
}

test("1/2 + 3/4");