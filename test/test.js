console.log(" 1068 - parenthesis balance I ");

const input = `a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)(
((((
())(()`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++){

    let data = lines[i].trim().split('');

    let parenthese = data.filter((char) => {
        return char == "(" || char == ")"
    });

    let haveParenthese = HaveParenthesis(parenthese);

    if ( haveParenthese == false ){
        break;

    } else if( haveParenthese == true ){

        console.log(parenthese)

        ValidByCount(parenthese);
        ValidFormat(parenthese);

        console.log(" ")

    }

};



function HaveParenthesis(parenthese){
    if(parenthese.length == null){
        return false
    } else {
        return true
    };
};


function ValidByCount(arry){

    let count = 0;

    for (let i = 0; i < arry.length; i++){

        if(arry[i] == "(" ){
            count++
        } else if ( arry[i] == ")" ){
            count--
        }
    };

    if( count == 0 ){
        return console.log('correct count');
    } else {
        return console.log('incorrect count');
    };

};

function ValidFormat ( arry ){

    let close = arry.filter(char => {
        return char == ")"
    });

    let open = arry.filter(char => {
        return char == "("
    });

    if ( arry.length % 2 == 0 && arry[0] == "(" && close.length == open.length ){
        return console.log('correct format')

    } else if ( arry[0] == ")" || arry.length % 2 != 0 || close.length !== open.length){
        return console.log('incorrect format')
    };

};


