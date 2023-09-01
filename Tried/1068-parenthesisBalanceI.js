console.log(" 1068 - parenthesis balance I ");

const input = `a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)(`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++){

    let data = lines[i].split('');

    let open = data.filter((char) => {
        return char == '('
    });

    let close = data.filter((char) => {
        return char == ')'
    });

    if(open.length == null && close.length == null){
        break;

    } else if(open.length == close.length && open.length !== null && close.length !== null){
        console.log('correct')

    } else if(open.length !== close.length) {
        console.log('incorrect')

    };

};