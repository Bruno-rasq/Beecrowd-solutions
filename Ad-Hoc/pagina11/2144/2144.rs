use std::io;

fn rep_maxima(peso: u32, reps: u32) -> f32 {
    return peso as f32 * (1.0 + (reps as f32 / 30.0));
}

fn main() {

    let mut input = String::new();
    let mut medias = Vec::new();

    loop {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();

        if input.trim() == "0 0 0" {
            break;
        }

        let data: Vec<u32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
        let (w1, w2, reps) = (data[0], data[1], data[2]);

        let w1_max = rep_maxima(w1, reps);
        let w2_max = rep_maxima(w2, reps);
        let media_rm = (w1_max + w2_max) / 2.0;

        medias.push(media_rm);

        if media_rm >= 1.0 && media_rm < 13.0 {
            println!("Nao vai da nao");
        } else if media_rm >= 13.0 && media_rm < 14.0 {
            println!("E 13");
        } else if media_rm >= 14.0 && media_rm < 40.0 {
            println!("Bora, hora do show! BIIR!");
        } else if media_rm >= 40.0 && media_rm <= 60.0 {
            println!("Ta saindo da jaula o monstro!");
        } else {
            println!("AQUI E BODYBUILDER!!");
        }
    }

    let mut media_geral: f32 = 0.0;
    for media in &medias {
        media_geral += media;
    }

    if !medias.is_empty() {
        media_geral /= medias.len() as f32;
    }

    if media_geral > 40.0 {
        println!("");
        println!("Aqui nois constroi fibra rapaz! Nao e agua com musculo!");
    }
}
