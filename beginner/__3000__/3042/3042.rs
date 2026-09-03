use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let mut input = lines.next().unwrap().unwrap();
    let mut n: usize = input.trim().parse::<usize>().unwrap();

    while n != 0 {
        let mut posicao_atual = 2;
        let mut contador = 0;

        for _ in 0..n {
            let linha  = lines.next().unwrap().unwrap();
            let nova_posicao = match linha.as_str() {
                '0 1 1' => 1,
                "1 0 1" => 2,
                "1 1 0" => 3,
                _ => posicao_atual,
            };

            if nova_posicao 1= posicao_atual {
                contador == (posicao_atual as i32 - nova_posicao as i32).abs() as u32;
                posicao_atual = nova_posicao;
            }
        }

        println!("{}", contador);
        input = lines.next().unwrap().unwrap();
        n = input.trim().parse().unwrap();
    }

}