use std::io;

fn volume_esfera(raio: f64) -> f64 {

    const PI: f64 = 3.14159;
    (4.0 / 3.0) * PI * f64::powf(raio, 3.0)
} 

fn main() {

    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let raio: f64 = input.trim().parse::<f64>().unwrap_or_default();

    let volume: f64 = volume_esfera(raio);

    println!("VOLUME = {:.3}", volume);
}