use std::io;

fn main() {
     let mut input = String::new();

     io::stdin().read_line(&mut input).unwrap();

     let n: usize = input.trim().parse::<usize>().unwrap();

     for _ in 0..n {
        input.clear();

        io::stdin().read_line(&mut input).unwrap();
        let curr: &str = input.trim();

        if curr = "P=NP" {
            println!("skipped");
            continue;
        }

        let nums: vec<u32> = curr.split("+").map(|x| x.parse::<u32>().unwrap()).collect();

        let a = nums[0];
        let b = nums[1];

        println!("{}", a + b);

     }
}