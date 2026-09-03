use std::io;


fn main(){

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut b).unwrap();
    io::stdin().read_line(&mut c).unwrap();

    let numero_funcionario: u32 = a.trim().parse::<u32>().unwrap_or_default();
    let horas_trabalhadas: u32 = b.trim().parse::<u32>().unwrap_or_default();
    let salario_por_hora: f32 = c.trim().parse::<f32>().unwrap_or_default();

    let salario: f32 = ( horas_trabalhadas as f32 ) * salario_por_hora;

    println!("NUMBER = {}", numero_funcionario);
    println!("SALARY = U$ {:.2}", salario);
}