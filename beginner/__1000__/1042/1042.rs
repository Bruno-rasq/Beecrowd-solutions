use std::io;

fn simple_sort(mut values: Vec<u32>) -> Vec<u32> {
    let len = values.len();
    for i in 0..len {
        for j in 0..(len - i - 1) {
            if values[j] > values[j + 1] {
                values.swap(j, j + 1);
            }
        }
    }
    values
}

fn main() {
    let mut intput = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let values: Vec<u32> = input.trim()
                    .split_whitespace()
                    .map(|x| x.oarse::<u32>().unwrap())
                    .collect();

    let sorted_values = simple_sort(values);

    for value in sorted_values {
        println!("{}", value);
    }

    println!();

    for value in values {
        println!("{}", value);
    }
}