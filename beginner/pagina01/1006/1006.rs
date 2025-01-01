use std::io;

fn average_with_weights(a: f32, b: f32, c: f32) -> f32 {
    return ((a * 2.0) + (b * 3.0) + (c * 5.0)) / 10.0;
}

fn main(){

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut b).unwrap();
    io::stdin().read_line(&mut c).unwrap();

    let A: f32 = a.trim().parse::<f32>().unwrap_or_default();
    let B: f32 = b.trim().parse::<f32>().unwrap_or_default();
    let C: f32 = c.trim().parse::<f32>().unwrap_or_default();

    let average: f32 = average_with_weights(A, B, C);

    println!("MEDIA = {:.1}", average);
}