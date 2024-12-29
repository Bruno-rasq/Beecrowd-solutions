use std::io;

fn main(){

    let mut a = String::new();
    let mut b = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut b).unwrap();

    let B: u32 = a.trim().parse::<u32>().unwrap_or_default();
    let G: u32 = b.trim().parse::<u32>().unwrap_or_default();

    let faltantes: i32 = (g as i32 / 2) - b as i32;
    
    if faltantes <= 0 {
        println!("Amelia tem todas bolinhas!");
    } else {
        println!("Faltam {} bolinha(s)", faltantes);
    }
}