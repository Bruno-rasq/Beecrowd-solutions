use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<f32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (A, B, C) = (data[0], data[1], data[2]);

    let perimetro = (A + B + C);
    let area = ((A + B) * C ) / 2.0;
    
    if A < (B + C) && B < ( A + C) && C < (A + B) {
        println!("Perimetro = {:.1}", perimetro);
    } else {
        println!("Area = {:.1}", area);
    }
}