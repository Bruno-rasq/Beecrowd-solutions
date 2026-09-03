use std::io;

fn bhaskara(a: f64, b: f64, delta: f64) {

    let r1: f64 = (-b + delta.sqrt()) / (2.0 * a);
    let r2: f64 = (-b - delta.sqrt()) / (2.0 * a);

    println!("R1 = {:.5}", r1);
    println!("R2 = {:.5}", r2);
}

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a, b, c) = (data[0], data[1], data[2]);
    let delta = b.powi(2) - (4.0 * a * c);

    if a != 0.0 && delta >= 0.0 { bhaskara(a, b, delta); } else { println!("Impossivel calcular"); }
}