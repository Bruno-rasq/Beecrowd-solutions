<?php

    function rep_max($peso, $reps){
        return $peso * (1 + ($reps / 30));
    }

    $medias = [];
    while(true){
        $input = readline();
        
        if ($input == "0 0 0") {
            break;
        }

        list($w1, $w2, $reps) = explode(" ", $input);
        $w1 = (int)$w1;
        $w2 = (int)$w2;
        $reps = (int)$reps;

        $w1_max = rep_max($w1, $reps);
        $w2_max = rep_max($w2, $reps);

        $media_rm = ($w1_max + $w2_max) / 2;
        $medias[] = $media_rm;

        if ($media_rm < 13) {
            echo "Nao vai da nao\n";
        } elseif ($media_rm >= 13 && $media_rm < 14) {
            echo "E 13\n";
        } elseif ($media_rm >= 14 && $media_rm < 40) {
            echo "Bora, hora do show! BIIR!\n";
        } elseif ($media_rm >= 40 && $media_rm <= 60) {
            echo "Ta saindo da jaula o monstro!\n";
        } else {
            echo "AQUI E BODYBUILDER!!\n";
        }
    }

    $media_total = array_sum($medias) / count($medias);
    if ($media_total > 40.0) {
        echo "\nAqui nois constroi fibra rapaz! Nao e agua com musculo!\n";
    }
?>
