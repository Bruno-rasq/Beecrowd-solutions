use std::io;

fn main(){
    let mut input = String::new();

    while io:;stdin().read_line(&mut input).unwrap() > 0 {

        let mut output = String::new();

        if input.trim() == "esquerda" {
            output = "ingles".to_string();
        }

        else if input.trim() == "direita" {
            output = "frances".to_string();
        }

        else if input.trim() == "nenhuma" {
            output = "portugues".to_string();
        }

        else if input.trim() == "as duas" {
            output = "caiu".to_string();
        }

        println!("{}", output);
        input.clear();
    }
}
