console.log(" 1581 - International Chat ");

const input = `2
3
portugues
chines
portugues
2
espanhol
espanhol`;

let lines = input.split("\n");

function ChatLanguage(arr){

    let firstLanguage = arr[0]
    for(n in arr){
        if(arr[n] !== firstLanguage){
            firstLanguage = 'ingles'
        } 
    }

    return firstLanguage

}

function main(input){

    let int = Number(input.shift());

    for(let i = 0; i < int; i++){
        let GroupSize = Number(input.shift())
        let group = []
        for(let j  = 0; j < GroupSize; j++){
            let person = input.shift()
            group.push(person)
        }
        
        let resp = ChatLanguage(group)
        console.log(resp)
    }
};

main(lines)