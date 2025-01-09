use std::io;

fn main() {
    let mut input = String::new();
     io::stdin().read_line(&mut input).unwrap();

     let data: u32 = input.trim().parse::<u32>().unwrap();

     let mut total_centavos = data * 100;

     let notas: [u32; 7] = [10000, 5000, 2000, 1000, 500, 200, 100];

     println!("{}", data);
     for &nota in &notas {
        let qnt_notas = total_centavos / nota;
        println!("{} nota(s) de R$ {:.0},00", qnt_notas, nota as f64 / 100.0);
        total_centavos %= nota;
     }
}