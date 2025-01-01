use std::io;

fn GDP(a: f64, b: f64) -> f64 {
    ((1.0 + a / 100.0) * (1.0 + b / 100.0) - 1.0) * 100.0
}

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<f64> = input.trim().split_whitespace()
                        .map(\x\ x.parse::<f64>(),unwrap())
                        .collect();

    let result: f64 = GDP(data[0], data[1]);

    println!("{:.6}", result);
}