<?php

while($tempo = (int) readline()){
    if ($tempo == 0) break;

    $ale = (int) ceil(7.0 * $tempo / 90);
    $bra = (int) floor($tempo / 90.0);

    echo "Brasil $bra x Alemanha $ale\n";
}