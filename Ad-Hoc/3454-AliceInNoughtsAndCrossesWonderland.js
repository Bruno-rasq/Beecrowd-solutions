console.log(" 3454 - Alice in Noughts and Crosses Wonderland ");

const input = `XXO`;
let lines = input.split('\n');
let test = lines.shift()

switch(test){

    case 'XOX':
        console.log('*');
        break;

    case 'XXO':
        console.log('Alice');
        break;

    case 'OXX':
        console.log('Alice');
        break;

    default:
        console.log('?');
        break;
};