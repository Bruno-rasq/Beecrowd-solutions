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