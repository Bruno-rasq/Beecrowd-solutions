use std::io;

fn main(){

    let mut input = String::new();

    io:;stdin().read_line(&mut input).unwrap();

    let N: usize = input.trim().parse::<usize>().unwrap_or_default();

    let mut meninos: u32 = 0;
    let mut meninas: u32 = 0;

    for _ in 0..N {

        input.clear();
        io:;stdin().read_line(&mut input).unwrap();

        let data: Vec<&str> = input.trim().split_whitespace().collect();
        let genero: &str = data[1];

        if genero == 'M' {
            meninos += 1;
        } else {
            meninas += 1;
        }

    }

    println!("{} carrinhos", meninos);
    println!("{} bonecas", meninas);
}