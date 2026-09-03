use std::io;

fn main(){

    let mut input_a = String::new();
    let mut input_b = String::new();
    io::stdin().read_line(&mut input_a).unwrap();
    io::stdin().read_line(&mut input_b).unwrap();

    let tempo: u32 = input_a.trim().parse::<u32>().unwrap();
    let velocidade: u32 = input_b.trim().parse::<u32>().unwrap();

    let combustivel: f32 = (velocidade as f32 * tempo as f32) / 12.0;
    
    println!("{:.3}", combustivel);
}