use std::io;

fn brute(n: u32) -> u32 {

    let decimais: [u32; 8] = {6, 6, 5, 5, 5, 7, 6, 6};

    let unitarios: [u32; 21] = {
        4, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3,
        6, 6, 8, 8, 7, 7, 9, 8, 8, 6
    };


    if n == 100{ 
        return 11; 
    }
    else if n <= 20 { 
        return unitarios[n]; 
    }
    else {
        let dec = n / 10;
        let uni = n % 10;
        let mut result = decimais[(dec - 2) as usize];
        if uni != 0 {
            result += unitarios[uni as usize];
        }
        return result;
    }
}

fn main() {
    let mut intput = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let mut n: u32 = input.trim().parse::<u32>().unwrap();

    for i in 0..1000 {
        n = brute(n);
    }

    println!("{}", n);
}