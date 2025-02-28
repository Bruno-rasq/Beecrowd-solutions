use std::io;

fn fixtext(text: &str) -> String {
    let mut fixed = String::new();
    let len = text.len();
    let chars: Vec<char> = text.chars().collect();

    for i in 0..len {
        let charac = chars[i];
        if i < len - 1 {
            let next = chars[i + 1];
            if charac == ' ' && (next == ',' || next == '.') {
                continue; 
            }
        }
        fixed.push(charac);
    }
    fixed
}

fn main() {
    let mut input = String::new();
    while io::stdin().read_line(&mut input).unwrap() > 0 {
        let output = fixtext(&input.trim());
        println!("{}", output);
        input.clear();
    }
}
