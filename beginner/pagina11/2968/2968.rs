use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse::<u32>().unwrap()).collect();

    let (voltas, placas) = (data[0], data[1]);
    let total_placas: u64 = voltas as u64* placas as u64;

    let mut output = String::new();

    for porcent in (10..=90).step_by(10) {
        let qnt_placas_por_porcentagem: u64 = ((total_placas * porcent) as f64 / 100.0).ceil() as u64;
        output.push_str(&qnt_placas_por_porcentagem.to_string());
        output.push(" ");
    }

    println!("{}", output.trim());
}