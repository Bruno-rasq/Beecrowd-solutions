use std::io;

fn main() {

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (pedido, quantidade) = (data[0], data[1]);

    let cardapio: [f32; 5] = [4.00, 4.50, 5.00, 2.00, 1.50];

    let preco = cardapio[pedido as usize - 1] * quantidade as f32;

    println!("Total: R$ {:.2}", preco);
}