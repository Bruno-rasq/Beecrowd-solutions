use std::io;

fn main() {

    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let n: u32 = input.trim().parse::<u32>().unwrap();
    let mut b: u32 = 0;
    let mut p: u32 = 0;

    if (n % 2 == 0){
        b = total_cases / 2;
        p = total_cases / 2;
    } else {
        b = (total_cases + 1) / 2;
        p = b - 1;
    }

    println!("{} casas brancas e {} casas pretas", b, p);
}