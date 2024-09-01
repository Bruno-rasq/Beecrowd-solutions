// const input = 
`Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');


const PrepareDate = (day: string, info: string) => {

    let [ string, Day ] = day.split(' ').map(el => Number(el))
    let Infos = info.split(' ').filter(el => {
        return el != ':'
    }).map(el => Number(el))

    const Date = {
        'Days': Day,
        'Hours': Infos[0],
        'Minutes': Infos[1],
        'Seconds': Infos[2]
    }

    return Date
}

const Convert = (day: number, hour: number, min: number, sec: number): number => {
    return (24 * 60 * 60) * day + (60 * 60) * hour + 60 * min + sec
}

const DefinitionDate = ( list: string[]): void => {

    
    let Initial = PrepareDate(`${list.shift()}`, `${list.shift()}`);
    let Final = PrepareDate(`${list.shift()}`, `${list.shift()}`);

    let Init_converte = Convert(Initial.Days, Initial.Hours, Initial.Minutes, Initial.Seconds);
    let End_converte = Convert(Final.Days, Final.Hours, Final.Minutes, Final.Seconds);

    
    let duration = End_converte - Init_converte

    console.log(`${Math.floor(duration / (24 * 60 * 60))} dia(s)`);
    duration %= (24 * 60 * 60)
    console.log(`${Math.floor(duration / (60 * 60))} hora(s)`);
    duration %= (60 * 60)
    console.log(`${Math.floor(duration / (60))} minuto(s)`);
    duration %= 60
    console.log(`${Math.floor(duration)} segundo(s)`);
}

DefinitionDate(lines)