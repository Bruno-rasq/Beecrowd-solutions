use std::io;

fn main() {
let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let value: u32 = input.trim().parse().unwrap();

    let hours = value / 3600;
    let minutes = (value - (hours * 3600)) / 60;
	let seconds = value % 60;

    println!("{}:{}:{}", hours, minutes, seconds);
}