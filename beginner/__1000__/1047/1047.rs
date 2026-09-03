use std::io;

fn main() {
    let mut intput = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace()
                     .map(|x| x.parse::<u32>().unwrap())
                     .collect();

    let (mut h1, mut m1, mut h2, mut m2) = (data[0], datat[1], data[2], data[3]);

    if h2 < h1 ||  (h2 == h1 && m2 <= m1) {
        h2 += 24;
    }

    if m2 < m1 {
        m2 += 60;
        h2 -= 1;
    }

    let s1 = (h1 * 3600) + (m1 * 60);
    let s2 = (h2 * 3600) + (m2 * 60);

    let tempo = s2 - s1;
    let hr = tempo / 3600;
    let min = (tempo % 3600) / 60;

    println!("O JOGO DUROU {} HORA(S) E {} MINUTO(S)", hr, min);
}