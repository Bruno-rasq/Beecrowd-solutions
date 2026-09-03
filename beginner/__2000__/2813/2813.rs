use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let n: usize = input.trim().parse::<usize>().unwrap();
    
    let mut guardachuvaCasa: i32 = 0;
    let mut guardachuvatrabalho: i32 = 0;
    let mut comprasCasa: i32 = 0;
    let mut comprasTrabalho: i32 = 0;
    
    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();

        let data: Vec<&str> = input.trim().split_whitespace().collect();
        let (ida, volta) = (data[0], data[1]);

        if ida == "chuva" {
            if guardachuvaCasa > 0 { guardachuvaCasa -= 1 } else { comprasCasa += 1 };
            guardachuvatrabalho += 1;
        }

        if volta == "chuva" {
            if guardachuvatrabalho > 0 { guardachuvatrabalho -= 1 } else { comprasTrabalho += 1 };
            guardachuvaCasa += 1;
        }
    }

    println!("{} {}", comprasCasa, comprasTrabalho);
}