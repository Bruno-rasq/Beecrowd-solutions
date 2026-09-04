<?php

list($a, $b, $c) = explode(" ", fgets(STDIN));
$nsoldados = (int) $c;
$coeficiente = (int) $b / (int) $a;
$hemisferioNorte = 0; $hemisferioSul = 0;

for($i = 0; $i < $nsoldados; $i++){
    list($x, $y, $p) = explode(" ", fgets(STDIN));
    if((int) $y > $coeficiente * (int) $x){
        $hemisferioNorte += (int) $p;
    } else {
        $hemisferioSul += (int) $p;
    }
}

echo "$hemisferioNorte $hemisferioSul\n";