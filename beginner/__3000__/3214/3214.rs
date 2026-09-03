use std::io;

fn main() {

     let mut input = String::new();

     io::stdin().read_line(&mut input).unwrap();

     let nums: vec<u32> = curr.split("+").map(|x| x.parse::<u32>().unwrap()).collect();

     let (mut e, g, f) = (nums[0], nums[1], nums[2]);

     let mut count: u32 = 0;

     e += f;

     while e >= f {
        e = e - f + 1;
        count += 1;
     }

     println!("{}", count);
     
}