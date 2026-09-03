use std::io;

fn sort(mut values: Vec<f64>) -> Vec<f64> {
    let len = values.len();
    for i in 0..len {
        for j in 0..(len - i - 1) {
            if values[j] > values[j + 1] {
                values.swap(j, j + 1);
            }
        }
    }
    values
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut data: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let data_sorted = sort(data);
    let (a, b, c) = (data_sorted[0], data_sorted[1], data_sorted[2]);

    let a2 = a.powi(2);
    let bc2 = b.powi(2) + c.powi(2);

    if a >= b + c {
        println!("NAO FORMA TRIANGULO");
        
    } else {
        if a2 == bc2 {
            println!("TRIANGULO RETANGULO");
        }
        if a2 > bc2 {
            println!("TRIANGULO OBTUSANGULO");
        }
        if a2 < bc2 {
            println!("TRIANGULO ACUTANGULO");
        }
        if a == b && b == c {
            println!("TRIANGULO EQUILATERO");
        }
        if (a == b && b != c) || (b == c && c != a) || (a == c && a != b) {
            println!("TRIANGULO ISOSCELES");
        }
    }
}
