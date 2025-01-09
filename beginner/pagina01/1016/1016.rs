use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let quilimetros: u32 = input.trim().parse::<u32>().unwrap();
    let tempo: u32 = quilimetros * 2;

    println!("{} minutos", tempo);
}