console.log(" 1068 - parenthesis balance I ");

const input = `a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)(
((((`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++){

    let data = lines[i].trim().split('');

    let parenthese = data.filter((char) => {
        return char == "(" || char == ")"
    });

    console.log(parenthese)

    let count = 0;

    for ( let n = 0; n < parenthese.length; n++){

        if(parenthese[n] == "("){
            count++
        } else if ( parenthese[n] == ")"){
            count--
        }
    };

    console.log(count)

    

};


