console.log(" 1256 - Hash Tables ");

const input = `2
13 9
44 45 49 70 27 73 92 97 95
7 8
35 12 2 17 19 51 88 86`;

let lines = input.split('\n');

class HashTable {

    constructor(size){
        this.size = size
        this.table = Array(size);
        for(let i = 0; i < this.size; i++){
            this.table[i] = []
        }
    };

    _hase(value){
        return value % this.size;
    };

    set(value){
        this.table[this._hase(value)].push(value)
    };

    print(){
        for(let i = 0; i < this.size; ++i){
            if(this.table[i].length > 0){
                console.log(`${i} -> ${this.table[i].join(' -> ')} -> \\`)
            } else {
                console.log(`${i} -> \\`)

            }
        }
    }
};

let int = Number(lines.shift());

for(let i = 0; i < int; ++i){
    if(i) console.log('');

    let [ M , C ] = lines.shift().trim().split(' ').map(el => Number(el));
    let line = lines.shift().trim().split(' ').map(el => Number(el));

    let ht = new HashTable(M)
    line.map(x => ht.set(x))
    ht.print()
}