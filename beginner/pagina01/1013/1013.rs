use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut data: Vec<u64> = input.trim().split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();

    //bubble sort
    for i in 0..3 {
        for j in 0..(3 - i - 1) {
            if data[j] > data[j + 1] {
                data.swap(j, j + 1);
            }
        }
    }

    println!("{} eh o maior", data[2]);
}