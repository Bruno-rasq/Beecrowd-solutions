use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let n: usize = input.trim().parse::<usize>().unwrap();
    let mut wins: u32 = 0;

    for i in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        if(!input.contains("CD")){
            wins+=1;
        }
    }

    println!("{}", wins);
}