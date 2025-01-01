use std::io;

fn main() {

    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let input_line1 = input.trim().to_string();
    let line1: Vec<&str> = input_line1.split_whitespace().collect();

    input.clear();

    io::stdin().read_line(&mut input).unwrap();
    let input_line2 =  input.trim().to_string();
    let line2 : Vec<&str> = input_line2.split_whitespace().collect();


    let quantidade1: u32 = line1[1].parse::<u32>().unwrap_or(0);
    let valor1 : f64 = line1[2].parse::<f64>().unwrap_or(0.0);

    let quantidade2: u32 = line2[1].parse::<u32>().unwrap_or(0);
    let valor2 : f64 = line2[2].parse::<f64>().unwrap_or(0.0);

    let valor_a_pagar = (quantidade1 as f64 * valor1) + (quantidade2 as f64 * valor2);

    println!("VALOR A PAGAR: R$ {:.2}", valor_a_pagar);
    
}