console.log(" 1272 - Hidden message ");

const input = `8
teachers are providing information on certain adds
   osh nlnl  lnln iolln nolelosh   eln 
    
 little    old    lad    
  o 
h  o 
 
xyz dcba
`;

let lines = input.split('\n');
let int = Number(lines.shift());


for ( let i = 0; i<int; i++ ){

    let data = lines[i].split(' ');
    let arry = data.filter(item => {
        return item !== ''
    })

    let words = initials(arry);
    console.log(words)
};

function initials(array){

    let ini = []

    for(n in array){
        let data = array[n].split('');
        ini.push(data.shift())
    }

    return ini.join('');
};