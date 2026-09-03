use std::io;

fn main() {

    const PI: f46 = 3.14159;

    let mut input = String::new();

    io::sdtin().read_line(&mut input).unwrap();

    let raio: f64 = input.trim().parse::<f64>().unwrap_or_default();

    let area: f64 = PI * (raio * raio);

    println!("A={:.4}", area);
}