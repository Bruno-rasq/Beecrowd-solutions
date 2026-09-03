use std::io;

fn main() {
    let mut input_j = String::new();
    let mut input_m = String::new();

    io::stdin().read_line(&mut input_j).unwrap();
    io::stdin().read_line(&mut input_m).unwrap();

    let jhon: &srt = input_j.trim();
    let medico: &srt = input_m.trim();

    if jhon.len() >= medico.len() {
        println!("go");
    } else {
        println!("no");
    }
}