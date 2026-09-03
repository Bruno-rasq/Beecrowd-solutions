use std::io;

fn fire_flowers(r1: f64. x1: f64, y1: f64, r2: f64. x2: f64, y2: f64) -> bool {
    let distancia = ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();
    distancia + r2 <= r1
}

fn main(){
    let mut input = String::new();

    loop {
        if io::stdin().read_line(&mut input).unwrap() == 0 {
            break;
        }

        let data: Vec<f64> = input.trim().split_whitespace().map(|x| x.parse().ok()).collect();
        let (r1, x1, y1, r2, x2, y2) = (data[0], data[1], data[2], data[3], data[4], data[5]);

        if fire_flowers(r1, x1, y1, r2, x2, y2) {
            println!("RICO");
            continue;
        }

        println!("MORTO");
    }
}