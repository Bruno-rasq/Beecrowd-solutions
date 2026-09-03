use std::io;

fn segmentos(n: f64) -> f64 {
    1.0 + (((n - 1.0) * n) / 2.0) + ((n * (n - 1.0) * (n - 2.0) * (n - 3.0)) / 24.0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let n: u32 = input.trim().parse::<u32>().unwrap();

    let segments = segmentos(n as f64);

    println!("{:.0}", segments);
}