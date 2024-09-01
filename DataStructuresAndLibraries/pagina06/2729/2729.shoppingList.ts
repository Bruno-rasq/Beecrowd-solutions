const input = `2
steak orange juice biscuit orange juice orange biscuit
aplle orange soap orange soap`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')


function main(): void {

   let int = Number(lines.shift())
   for(let i = 0; i< int; i++){

        let currList = String(lines[i])
                    .split(' ')
                    .sort((a, b) => a.localeCompare(b))

        let filtered: string[] = []
        currList.forEach(item => {
            if(!filtered.includes(item)){
                filtered.push(item)
            }
        })

        console.log(filtered.join(' '))
   }

}

main()