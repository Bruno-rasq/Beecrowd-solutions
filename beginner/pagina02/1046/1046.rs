use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a,  b) = (data[0], data[1]);
    let mut resp = 0;
    
    if a > b || a== b {
        resp = (24 - a) + b;
    } else {
        resp = b - a;
    }

    println!("O JOGO DUROU {} HORA(S)", resp);
}