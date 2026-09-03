const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

// -------------  ESTRUTURAS DE DADOS ----------------

// stack: first-in, last-out
// queue: first-in, first-out
// priority-queue: maxvalues-first-out
// not sure: queue | stack | priority
// impossible: !queue && !stack && !priority

class DataStructure {

    constructor(){
        this.elements = [] 
        this.booleanRemoved = [] 
    }

    isEmpty(){
        return this.elements.length === 0
    }

    throw_in(val){
        this.elements.push(val)
    }

    compare(){
        return this.booleanRemoved.every(valor => valor === 1)
    }
}

class Queue extends DataStructure {

    take_out(value) {
        if(!this.isEmpty()){
            if(value == this.elements[0]){
                this.elements = this.elements.filter(element => element !== value)
                this.booleanRemoved.push(1)
                return
            }
            this.booleanRemoved.push(0)
        }
    }
}

class Stack extends DataStructure {

    take_out(value){
        if(!this.isEmpty()){
            if(value == this.elements[this.elements.length - 1]){
                this.elements = this.elements.filter(element => element !== value)
                this.booleanRemoved.push(1)
                return
            }
            this.booleanRemoved.push(0)
        }
    }
}

class Priority_queue extends DataStructure {

    take_out(value){
        if(!this.isEmpty()){
            let max = Math.max(...this.elements)
            if(value == max){
                let index = this.elements.indexOf(max)
                this.elements = this.elements.filter(element => element != this.elements[index])
                this.booleanRemoved.push(1)
                return
            }
            this.booleanRemoved.push(0)
        }
    }

}


// run code...
Main(lines)


function Main(arr){

    while(arr.length){

        let int = Number(arr.shift())
        let Data = []

        if(int === 0) break

        for(let i = 0; i < int; i++){
            Data.push(String(arr.shift()))
        }

        i_can_guess_the_data_structure(Data)
    }
}

function i_can_guess_the_data_structure(list){

    let stack = new Stack();
    let queue = new Queue();
    let priority = new Priority_queue();


    function add(val){
        stack.throw_in(val)
        queue.throw_in(val)
        priority.throw_in(val)
    }

    function remove(val){
        stack.take_out(val)
        queue.take_out(val)
        priority.take_out(val)
    }

    for(let i = 0; i < list.length; i++){
        let [ command, value ] = list[i].split(' ').map(el => Number(el))

        // 1 throw In || 2 take out
        command == 1 ? add(value) : remove(value)
    }

    OUTPUT([stack.compare(), queue.compare(), priority.compare()])
}

function OUTPUT(arr){

    let dataStructure = ['stack', 'queue', 'priority queue']
    let countTrue = arr.filter(el => el).length;

    if(countTrue == 0){
        console.log('impossible')

    } else if (countTrue > 1){
        console.log('not sure')

    } else {
        let index = arr.indexOf(true)
        console.log(dataStructure[index])
    }
}