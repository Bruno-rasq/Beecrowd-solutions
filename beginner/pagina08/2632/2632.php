<?php 

    $spells = [
        ["fire", 200, [20, 30, 50]],
        ["earth", 400, [25, 55, 70]],
        ["water", 300, [10, 25, 40]],
        ["air", 100, [18, 38, 60]],
    ];

    $t = (int) readline();

    for($i = 0; $i < $t; $i++){

        list($w, $h, $x0, $y0) = explode(" ", readline());
        list($magia, $nivel, $cx, $cy) = explode(" ", readline());

        $w = (int) $w;
        $h = (int) $h;
        $x0 = (int) $x0;
        $y0 = (int) $y0;
        $nivel = (int) $nivel;
        $cx = (int) $cx;
        $cy = (int) $cy;

        $curr_spell = [];
        foreach($spells as $spell){
            if($spell = $magia){
                $curr_spell = $spell;
                break;
            }
        }

        $dano = $curr_spell[1];
        $raio = $curr_spell[2][$nivel - 1];

        $left = $x0; $rigth = $x0 + $w; $bottom = $y0; $top = $y0 + $h;

        $closestX = max($left, min($cx, $right));
        $closestY = max($bottom, min($cy, $top));

        $distancia = ($closestX - $cx) * ($closestX - $cx) + ($closestY - $cy) * ($closestY - $cy);

        if($distancia <= $raio * $raio){
            echo "$dano\n";
        } else {
            echo "0\n";
        }
    }
?>