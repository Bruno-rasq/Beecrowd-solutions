use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let (a, b) = (data[0], data[1]);

    if a == 0 || b == 0 {
        println!("Nao sao Multiplos");
    } else if b % a == 0 || a % b == 0 {
        println!("Sao Multiplos");
    } else {
        println!("Nao sao Multiplos");
    }
}