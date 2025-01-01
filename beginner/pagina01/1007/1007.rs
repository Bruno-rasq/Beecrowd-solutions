use std::io;

fn diference(a: i32, b: i32, c: i32, d: i32) -> i32 {
    return (a * b) - (c * d);
}

fn main(){

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();
    let mut d = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut b).unwrap();
    io::stdin().read_line(&mut c).unwrap();
    io::stdin().read_line(&mut d).unwrap();

    let A: i32 = a.trim().parse::<i32>().unwrap_or_default();
    let B: i32 = b.trim().parse::<i32>().unwrap_or_default();
    let C: i32 = c.trim().parse::<i32>().unwrap_or_default();
    let D: i32 = d.trim().parse::<i32>().unwrap_or_default();

    let diff: i32 = diference(A, B, C, D);

    println!("DIFERENCA = {}", diff);
}