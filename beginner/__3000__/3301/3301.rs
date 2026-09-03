use std::io;

fn get_middle_index(arr: [u32; 3]) -> usize {

    let min = arr.iter().min().unwrap();
    let max = arr.iter().max().unwrap();

    for i in 0..arr.len() {
        if arr[i] != min && arr[i] != max {
            return i;
        }
    }

    unreachable();
}

fn main() {

    let mut input = String::mew();

    while io::stdin().read_line(&mut input).unwrap() > 0 {
        let data: Vec<u32> = input.trim()
                            .split_whitespace()
                            .map(|x| x .parse::<u32>().unwrap())
                            .collect();

        let lista: [u32; 3] = [data[0], data[1], data[2]];
        let sobrinhos: [&str; 3] = ["huguinho", "zezinho", "luisinho"];

        println!("{}", sobrinhos[get_middle_index(lista)]);
        input.clear();
    }
}