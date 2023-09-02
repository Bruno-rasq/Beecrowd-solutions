console.log(" 1068 - parenthesis balance I ");

const input = `a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)(`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++){

    let data = lines[i].trim().split('');

    let parenthese = data.filter((char) => {
        return char == "(" || char == ")"
    });

    let close = parenthese.filter(char => {
        return char == ")"
    });

    let open = parenthese.filter(char => {
        return char == "("
    });

    if ( parenthese.length == null ){
        break;

    } else if ( parenthese.length % 2 == 0 && parenthese[0] == "("  && open.length == close.length ){
        console.log('correct');

    } else if ( parenthese[0] == ")" && parenthese.length % 2 == 0 ){
        console.log("incorrect");

    } else if ( parenthese.length % 2 !== 0 || open.length !== close.lenght){
        console.log('incorrect');
    };

};


/*
    PROBLEMA:
        - código está fazendo o que devia porém com um erro

        - se a quantidade de abertura de parenteses for igual a de fechamento
        basicamente quer dizer que está certo mas tecnicamente não assegura que a formatação estaja tbm.

        (  ( )  -> incorreto

        ")" "( )" "(" -> nesse caso a qnt de abertura e fechamento é igual porem a formatação está incorreta

    NOTA:
        - concertei o problema da formatação de parenteses e mesmo assim não passou no teste

*/