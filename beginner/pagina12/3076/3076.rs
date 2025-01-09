use std::io;

fn main() {

    let mut input = String::new();

    while io::stdin().read_line(&mut input).unwrap() > 0 {

        let ano: u32 = input.trim().parse().unwrap();

        let seculo = if ano % 100 == 0 { ano / 100 } else { ano / 100 + 1 };

        println!("{}", seculo);

        input.clear();
    } 
}