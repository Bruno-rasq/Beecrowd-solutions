use std::io;

fn main() {
    let mut total_pecas = String::new();
    io::stdin().read_line(&mut total_pecas).unwrap();
    let total_pecas: u32 = total_pecas.trim().parse().unwrap();
    
    let mut data = String::new();
    io::stdin().read_line(&mut data).unwrap();

    let pecas: Vec<u32> = data.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();

    for i in 1..=total_pecas {
        let mut encontrou = false;

        for j in 0..pecas.len() {
            if pecas[j] == i {
                encontrou = true;
                break;
            }
        }

        if !encontrou {
            println!("{}", i);
            break;
        }
    }
}
