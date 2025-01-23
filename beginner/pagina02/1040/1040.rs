use std::io;

fn main(){

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let notas: Vec<f32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let media = ((notas[0] * 2.0) + (notas[1] * 3.0) + (notas[2] * 4.0) + (notas[3] * 1.0)) / 10.0;
    
    println!("Media: {:.1}", media);
    
    if media >= 7.0 { println!("Aluno aprovado."); } else if media < 5.0 { println!("Aluno reprovado."); }
    else {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let exame: f32 = input.trim().parse().unwrap();

        println!("Aluno em exame.");
        println!("Nota do exame: {:.1}", exame);

        let media_com_exame = (media + exame) / 2.0;

        if media_com_exame >= 5.0 { println!("Aluno aprovado."); } 
        else if media < 5.0 { println!("Aluno reprovado."); }

        println!("Media final: {:.1}", media_com_exame);
    }
}