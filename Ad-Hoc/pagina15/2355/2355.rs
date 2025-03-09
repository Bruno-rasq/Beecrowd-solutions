use std::io;

fn main() {
    let mut input = String::new();
    
    while io::stdin().read_line(&mut input).is_ok() {
        let tempo: i32 = match input.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        if tempo == 0 {
            break;
        }

        let ale = (7.0 * tempo as f64 / 90.0).ceil() as i32;
        let bra = (tempo as f64 / 90.0).floor() as i32;

        println!("Brasil {} x Alemanha {}", bra, ale);
        
        input.clear(); // Limpa o buffer para a próxima entrada
    }
}