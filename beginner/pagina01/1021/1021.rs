use std::io;

fn main() {
     let mut input = String::new();
     io::stdin().read_line(&mut input).unwrap();

     let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse::<u32>().unwrap()).collect();

     let mut total_centavos = data[0] * 100 + data[1];

     let notas: [u32; 6] = [10000, 5000, 2000, 1000, 500, 200];
     let moedas: [u32; 6] = [100, 50, 25, 10, 5, 1];

     println!("NOTAS:");
     for &nota in &notas {
        let qnt_notas = total_centavos / nota;
        println!("{} nota(s) de R$ {:.2}", qnt_notas, nota as f64 / 100.0);
        total_centavos %= nota;
     }
     println!("MOEDAS:");
     for &moeda in &moedas {
        let qnt_moedas = total_centavos / moeda;
        println!("{} moeda(s) de R$ {:.2}", qnt_moedas, moeda as f64 / 100.0);
        total_centavos %= moeda;
     }

}