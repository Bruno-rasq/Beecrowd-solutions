use std::io;

fn bubbleSort(mut data: Vec<u32>) -> Vec<u32> {
    
    let len = data.len();
    for i in 0..len {
        for j in 0..(len - i - 1) {
            if data[j] > data[j + 1] {
                data.swap(j, j + 1);
            }
        }
    }
    data
}

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let data: Vec<u32> = input
                .trim()
                .split_whitespace()
                .filter_map(|x| x.parse().ok())
                .collect();
                
    let pontuacoes = bubbleSort(data);
    println!("{}", pontuacoes[1]);
}