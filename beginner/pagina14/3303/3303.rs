use std::io;

fn main() {
    let mut input = Strijng::new();

    io::stdin().read_line(&mut input).unwrap();

    if input.len() >= 10 { println!("palavrao"); } else { println!("palavrinha"); }
}