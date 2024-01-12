const input = `5 3
Maria
João
Carlos
Vanessa
Jose`;

let lines = input.split('\n');

const  callList = (data) => {

    let [ props, ...list] = data
    let [n, p] = props.split(' ')

    const sortedList = list
                        .slice(0, +n)
                        .sort((a, b) => a.localeCompare(b))

    console.log(sortedList[+p - 1])
}

callList(lines)