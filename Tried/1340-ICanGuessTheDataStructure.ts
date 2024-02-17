const input = `6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4`
  
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

class DataStructure {

    protected elements: number[] = []

    isEmpty(): boolean{
        return this.elements.length === 0
    }

    throw_in(val: number): void{
        this.elements.push(val)
    }
}

class Queue extends DataStructure {

    take_out(value: number): void {
        if(!this.isEmpty()){
            if(value == this.elements[0]){
                this.elements = this.elements.filter(element => element !== value)
            }
        }
    }
}

class Stack extends DataStructure {

    take_out(value: number): void {
        if(!this.isEmpty()){
            if(value == this.elements[this.elements.length - 1]){
                this.elements = this.elements.filter(element => element !== value)
            }
        }
    }
}

class Priority_queue extends DataStructure {

    take_out(value: number): void {
        if(!this.isEmpty()){
            let max = Math.max(...this.elements)
            if(value == max){
                let index = this.elements.indexOf(max)
                this.elements = this.elements.filter(element => element != this.elements[index])
            }
        }
    }
}

Setup_data_structure(lines)

function Setup_data_structure(arr: string[]): void{

    while(arr.length){

        let int = Number(arr.shift())
        let Data: any[] = []

        for(let i = 0; i < int; i++){
            let num = arr.shift()
            Data.push(num)
        }

        i_can_guess_the_data_structure(Data)
    }
}

// 1 throw In || 2 take out

// stack first-in, last-out
// queue first-in, first-out
// priority-queue maxvalues-first-out
// not sure queue | stack | priority
// impossible !queue && !stack && !priority

function i_can_guess_the_data_structure(list: string[]): void {

    let stack = new Stack();
    let queue = new Queue();
    let priority = new Priority_queue();

    function add(val: number){
        stack.throw_in(val)
        queue.throw_in(val)
        priority.throw_in(val)
    }

    function remove(val: number){
        stack.take_out(val)
        queue.take_out(val)
        priority.take_out(val)
    }
    
    list.forEach(element => {
        let [ command, value ] = element.split(' ')
        
        Number(command) == 1 ? add(Number(value)) : remove(Number(value))
    })

    response([stack.isEmpty(), queue.isEmpty(), priority.isEmpty()])
}

function response(arr: boolean[]): void {

    let dataStructure = ['stack', 'queue', 'priority queue']
    let countTrue = arr.filter(el => el).length;

    if(countTrue > 1 && countTrue !== 3){
        console.log('not sure')

    } else if (countTrue == 3 || countTrue == 0){
        console.log('impossible')

    } else {
        let index = arr.indexOf(true)
        console.log(dataStructure[index])
    }
}