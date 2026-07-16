use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    // Remove '\n' e '\r'
    let input = input.trim();

    let bytes = input.as_bytes();

    let mut i: usize = 0;
    let mut f: usize = bytes.len() - 1;
    let mut is_palindrome = true;

    while i < f {
        if bytes[i] != bytes[f] {
            is_palindrome = false;
            break;
        }
        i += 1;
        f -= 1;
    }

    if is_palindrome {
        println!("A frase [{}] eh palindrome", input);
    } else {
        println!("A frase [{}] nao eh palindrome", input);
    }
}