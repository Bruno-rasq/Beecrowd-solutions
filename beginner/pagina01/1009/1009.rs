use std::io;

fn calcular_bonus(valor: f64) -> f64 {
    return (15.0 * valor) / 100.0;
}

fn main() {

    let mut a = String::new();
    let mut b = String::new();
    let mut c = String::new();

    io::stdin().read_line(&mut a).unwrap();
    io::stdin().read_line(&mut b).unwrap();
    io::stdin().read_line(&mut c).unwrap();

    let salario_fixo: f64 = b.trim().parse::<f64>().unwrap_or_default();
    let valor_vendas: f64 = c.trim().parse::<f64>().unwrap_or_default();

    let salario: f64 = calcular_bonus(valor_vendas) + salario_fixo;

    println!("TOTAL = R$ {:.2}", (salario * 100.0).round() / 100.0);
}