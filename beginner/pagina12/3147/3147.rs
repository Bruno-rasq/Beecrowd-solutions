use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse::<u32>().unwrap()).collect();

    let (mut h, mut e, mut a, mut o, mut w, mut x) = (data[0], data[1], data[2], data[3], data[4], data[5]);

    if (h + e + a + x) >= (o + w){
        println!("Middle-earth is safe.");
    } else {
        println!("sauron has returned.");
    }
}