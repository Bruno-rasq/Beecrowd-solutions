use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut value: u32 = input.trim().parse().unwrap();

    let ages = value / 365;
	value %= 365;

	let months = value / 30;
	value %= 30;

	let days = value;

	println!("{} ano(s)", ages);
	println!("{} mes(es)", months);
	println!("{} dia(s)", days);
}