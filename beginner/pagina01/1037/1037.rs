use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let a: f32 = input.trim().parse().unwrap();

    if a >= 0.0 && a <= 25.0  {  println!("Intervalo [0,25]"); }
	if a > 25.0 && a <= 50.0  {  println!("Intervalo (25,50]"); }
	if a > 50.0 && a <= 75.0  {  println!("Intervalo (50,75]"); }
	if a > 75.0 && a <= 100.0 {  println!("Intervalo (75,100]"); }
	if a > 100.0 || a < 0.0   {  println!("Fora de intervalo"); }
}