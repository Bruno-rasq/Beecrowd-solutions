const input = `9
Kepeumo 67
Necoi 62
Seies 77
Ciule 49
Gyun 99
Finron 27
Norandir 66
Galvaindir 55
Pinhuobor 70`
  
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

interface gnomo {
    name: string
    age: number
}

namespace SETUP {

    const Set_gnomes = (arr: string[]): gnomo[] => {

        let gnomes = arr.map(gnomo => {

            let [name, age] = gnomo.split(' ') 
            return { name: name, age: Number(age)}

        }).sort((a, b) => {

            if(b.age !== a.age){
                return b.age - a.age
            }

            return a.name.localeCompare(b.name)
        })

        return gnomes
    }

    const Set_teams = (int: number, list: gnomo[]): string[][] => {

        let numberTeams = (int / 3)
        let Teams: string[][] = Array.from({length: numberTeams}, () => [])

        for(let i = 0; i < int; i++){
            let subIndex = (i % numberTeams)
            let { name, age } = list[i]
            Teams[subIndex].push(`${name} ${age}`)
        }

        return Teams
    }

    export const set_gnomes_team = (arr: string[]): string[][] => {
       
        let int = Number(arr.shift())
        let Gnomes = Set_gnomes(arr)
        let Teams = Set_teams(int, Gnomes)

        return Teams
    }
}

namespace OUTPUT {

    export const log = (arr: string[][]): void => {


        for(let i = 0; i < arr.length; i++){
            console.log(`Time ${i + 1}`)
            for(const gnomo of arr[i]){
                console.log(gnomo)
            }

            if(i < arr.length - 1){
                console.log()
            }
        }

    }

}


OUTPUT.log(SETUP.set_gnomes_team(lines))