<?php

function media_frase($frase){
    $somatorio = 0;
    $total = 0;

    foreach ($frase as $palavra){
        if(str_ends_with($palavra, ".")){
            $palavra = substr($palavra, 0 , -1);
        }

        if(ctype_alpha($palavra)){
            $somatorio += strlen($palavra);
            $total++;
        }
    }

    if($total == 0) return 0;

    return intdiv($somatorio, $total);
}

while(($frase = explode(" ", readline())) != false){

    $media = media_frase($frase);

    echo ($media <= 3 ? 200 : ($media > 3 && $media <= 5 ? 500 : 1000)) . "\n";
}