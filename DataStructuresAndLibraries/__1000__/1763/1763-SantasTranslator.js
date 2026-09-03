console.log(" 1763 - Santa's Translator ");

const input = `uri-online-judge
alemanha
brasil
austria`;

let lines = input.split('\n')

// database

let databank = `brasil              Feliz Natal!
alemanha            Frohliche Weihnachten!
austria             Frohe Weihnacht!
coreia              Chuk Sung Tan!
espanha             Feliz Navidad!
grecia              Kala Christougena!
estados-unidos      Merry Christmas!
inglaterra          Merry Christmas!
australia           Merry Christmas!
portugal            Feliz Natal!
suecia              God Jul!
turquia             Mutlu Noeller
argentina           Feliz Navidad!
chile               Feliz Navidad!
mexico              Feliz Navidad!
antardida           Merry Christmas!
canada              Merry Christmas!
irlanda             Nollaig Shona Dhuit!
belgica             Zalig Kerstfeest!
italia              Buon Natale!
libia               Buon Natale!
siria               Milad Mubarak!
marrocos            Milad Mubarak!
japao               Merii Kurisumasu!`;

let dbLines = databank.split('\n')
let DB = {}

for(n in dbLines){
    let [lang,  ...rest] = dbLines[n].replace(/( )+/g, " ").split(' ')
    DB[lang] = rest.join(' ')
}


let t = 0;
while(t < lines.length){
    let response = DB[lines[t]]

    if(response === undefined){
        console.log(`--- NOT FOUND ---`)
    } else {
        console.log(response)
    }

    t++
}