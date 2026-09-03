use std::io;

fn main() {

    let possibilidades: [u64; 14] = [
        0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 
        1588356, 8676360, 47977776, 266378112, 1488801600
    ];

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let t: usize = input.trim().parse().unwrap_or(0);

    for _ in 0..t {
        input.clear();
        
        io::stdin().read_line(&mut input).unwrap();
        let n: usize = input.trim().parse().unwrap_or(0);

        println!("{}", possibilidades[n - 1]);
    }
}