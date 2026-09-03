use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<f32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a, b) = (data[0], data[1]);

    if a == 0.0 && b == 0.0       { println!("Origem"); }
    else if  a == 0.0               { println!("Eixo Y");}
    else if  b == 0.0               { println!("Eixo X");}
    else if  b > 0.0 && a > 0.0     { println!("Q1");}
    else if  b > 0.0 && a < 0.0     { println!("Q2");}
    else if  b < 0.0 && a < 0.0     { println!("Q3");}
    else if  b < 0.0 && a > 0.0     { println!("Q4");}
    
}