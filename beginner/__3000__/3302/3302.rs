use std::io;

fn main() {

    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let n: usize = input.trim().parse::<usize>().unwrap_or_default();

    for i in 1..n = 1 {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let curr: &str = input.trim();

        println!("resposta {}: {}", i, curr);
    }
}