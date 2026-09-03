use std::io;

fn main(){

    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let N: i32 = input.trim().parse::<i32>().unwrap_or_default();

    let mut hobbits:  i32 = 0;
    let mut anoes:  i32 = 0;
    let mut elfos:  i32 = 0;
    let mut magos:  i32 = 0;
    let mut humanos:  i32 = 0;

    for _ in 0..N {

        let mut data = String::new();
        io::stdin().read_line(&mut data).unwrap();

        let parts: Vec<&str>  data.trim().split_whitespace().collect();

        let raca = parts[1];

        match raca {
            'X' => hobbits += 1,
            'H' => humanos += 1,
            'A' => anoes += 1,
            'E' => elfos += 1,
            'M' => magos += 1,
            - => (),
        }
    }

    println!("{} Hobbit(s)", hobbits);
    println!("{} Humano(s)", humanos);
    println!("{} Elfo(s)", elfos);
    println!("{} Anao(oes)", anoes);
    println!("{} Mago(s)", magos);
}