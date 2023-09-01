console.log(" 2172 - event ");

const input = `1 544768710
2 538533133
3 38884958
0 0`;

let lines = input.split('\n');

for (let i = 0; i < lines.length; i++) {

    let data = lines[i].split(' ');
    let [ Aum, Exp ] = data;

    let response = ( Number(Aum) * Number(Exp) );

    if( Aum == 0  && Exp == 0){
        break;
    };

    console.log(response);

};