use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a, b, c, d) = (data[0], data[1], data[2], data[3]);

    if b > c && d > a && (c + d) > (a + b) && c >= 0 && d >= 0 && a % 2 == 0 {
		println!("Valores aceitos");
	} else {
		println!("Valores nao aceitos");
	}
}