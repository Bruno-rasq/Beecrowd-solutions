use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let data: Vec<i32> = input
        .trim()
        .split_whitespace()
        .filter_map(|x| x.parse().ok())
        .collect();
    
    let (x, y) = (data[0], data[1]);
    let quo: i32;

    if (x > 0 && y > 0) || (x < 0 && y > 0) {
        quo = (x as f32 / y as f32).floor() as i32;
    } else {
        quo = (x as f32 / y as f32).ceil() as i32;
    }

    let remainder = x - (y * quo);

    println!("{} {}", quo, remainder);
}