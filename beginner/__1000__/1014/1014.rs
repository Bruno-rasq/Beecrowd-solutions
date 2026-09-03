use std::io;

fn main() {

    let mut input_a = String::new();
    let mut input_b = String::new();

    io::stdin().read_line(&mut input_a).unwrap();
    io::stdin().read_line(&mut input_b).unwrap();

    let distancia: u64 = input_a.trim().parse::<u64>().unwrap();
    let combustivel: f64 = input_b.trim().parse::<f64>().unwrap();

    let km: f64 = distancia as f64 / combustivel;

    println!("{:.3} km/l", km);
}