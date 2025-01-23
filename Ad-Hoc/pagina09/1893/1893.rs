use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (porcent2, porcent2) = (data[0], data[1]);

    if porcent2 <= 2 && porcent2 >= 0 { println!("nova");}

    else if porcent2 <= 100 && porcent2 >= 97 {  println!("cheia"); }

    else if porcent1 < porcent2 { println!("crescente"); } else { println!("minguante"); }
}