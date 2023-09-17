console.log(" 1272 - Hidden message ");

const input = `4
compete·online·design·event·rating
··u····r·i··o····n·l··i····n··e···
·
round··elimination·during··onsite··contest`;

let lines = input.split('\n');
let int = Number(lines.shift());


for ( let i = 0; i<int; i++ ){

    let data = lines[i].split('·');
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
