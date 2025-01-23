<?php 
    list($a, $b, $c, $d) = explode(" ", readline());

    $a = (float) $a;
    $b = (float) $b;
    $c = (float) $c;
    $d = (float) $d;

    $media = (($a * 2) + ($b * 3) + ($c * 4) + ($d * 1)) / 10;

    $media = floor($media * 10) / 10;
    echo "Media: " . number_format($media, 1, ".", "") . "\n";

    if ($media >= 7.0) { echo "Aluno aprovado.\n";} 
    elseif ($media < 5.0) { echo "Aluno reprovado.\n";}
    else {
        
        $exame_extra = (float) readline();

        echo "Aluno em exame.\n";
        echo "Nota do exame: " . number_format($exame_extra, 1, ".", "") . "\n";

        $media_com_exame = ($media + $exame_extra) / 2;
        $media_com_exame = floor($media_com_exame * 10) / 10;

        if ($media_com_exame >= 5.0) {echo "Aluno aprovado.\n";} else {echo "Aluno reprovado.\n";}
        echo "Media final: " . number_format($media_com_exame, 1, ".", "") . "\n";
    }

?>
