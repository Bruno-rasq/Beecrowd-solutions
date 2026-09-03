use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse::<f64>().unwrap()).collect();

    let (mut a, mut b, mut c) = (data[0], data[1], data[2]);

    let triangulo: f64 = (a * c) / 2.0;
    let circulo: f64 = (c * c) * 3.14159;
    let trapezio: f64 = ((a + b) * c) / 2.0;
    let quadrado: f64 = b * b;
    let retangulo: f64 = a * b;

    println!("TRIANGULO: {:.3}", triangulo );
    println!("CIRCULO: {:.3}", circulo);
    println!("TRAPEZIO: {:.3}", trapezio);
    println!("QUADRADO: {:.3}", quadrado);
    println!("RETANGULO: {:.3}", retangulo);
}