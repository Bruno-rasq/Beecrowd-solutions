use std::io;

fn main(){

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut B).unwrap();
    io::stdin().read_line(&mut c).unwrap();

    let a: char = a.trim().chars().next().unwrap_or_default();
    let B: char = b.trim().chars().next().unwrap_or_default();
    let c: char = c.trim().chars().next().unwrap_or_default();

    let array: [char; 3] = [a, b, c];
    let mut index: uszie = 0;

    for _ in 0..3 {

        let A = array[index];
        let B = array[(index + 1) % 3];
        let C = array[(index + 2) % 3];

        println!("A = {}, B = {}, C = {}", A, B, C);
        index = (index + 1) % 3;
    }

}