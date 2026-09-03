use std::io;

fn main() {

    let mut input_a = String::new();
    let mut input_b = String::new();

    io::stdin().read_line(&mut input_a).unwrap();
    io::stdin().read_line(&mut input_b).unwrap();

    let A: f64 = input_a.trim().parse::<f64>().unwrap_or_default();
    let B: f64 = input_b.trim().parse::<f64>().unwrap_or_default();

    let result: f64 = ((A * 3.5) + (B * 7.5)) / 11.0;

    println!("MEDIA = {;.5}", result);
}