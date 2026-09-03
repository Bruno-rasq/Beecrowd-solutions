use std::io;

fn jogadaPossivel(pi: &str, pd: &str) -> bool {
   
    let deslocamentos: [[i32; 2]; 8] = [
        [2, 1], [1, 2], [-1, 2], [-2, 1], 
        [-2, -1], [-1, -2], [1, -2], [2, -1]
    ];

    let coluna = (pi.chars().nth(0).unwrap() as u8 - b'a' + 1) as u32;
    let linha = pi.chars().nth(1).unwrap().to_digit(10).unwrap();

    let colunad = (pd.chars().nth(0).unwrap() as u8 - b'a' + 1) as u32;
    let linhad = pd.chars().nth(1).unwrap().to_digit(10).unwrap();

    for &[dx, dy] in deslocamentos.iter() {
        let nova_coluna = coluna as i32 + dx;
        let nova_linha = linha as i32 + dy;

        if nova_coluna == colunad as i32 && nova_linha == linhad as i32 {
            return true;
        }
    }

    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<&str> = input.trim().split_whitespace().collect();
    let (pi, pd) = (data[0], data[1]);

    let response: bool = jogadaPossivel(pi, pd);

    println!("{}", if response { "VALIDO" } else { "INVALIDO" });
}
