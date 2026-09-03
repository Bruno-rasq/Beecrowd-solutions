use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let data1: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse::<f64>().unwrap()).collect();
    
    input.clear();
    io::stdin().read_line(&mut input).unwrap();

    let data2: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse::<f64>().unwrap()).collect();

    let (x1, y1) = (data1[0], data1[1]);
    let (x2, y2) = (data2[0], data2[1]);

    let distancia: f64 = ((x2 - x1).powf(2.0) + (y2 - y1).powf(2.0)).sqrt();

    println!("{:.4}", distancia);
}