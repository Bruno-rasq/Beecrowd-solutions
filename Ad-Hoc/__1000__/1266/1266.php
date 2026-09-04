<?php

while (true) {
    $n = (int) readline();
    if ($n === 0) break;
    
    $z = 0;
    $s = 0;
    $i = 0;
    $p = 0;
    
    $postes = explode(" ", trim(readline()));
    foreach ($postes as $poste) {
        if ($poste == "0" && $i == 0) {
            $z++;
            $p++;
        } elseif ($poste == "0" && $i == 1) {
            $p++;
        } elseif ($poste == "1") {
            $i = 1;
            $s += floor($p / 2);
            $p = 0;
        }
    }
    
    if ($p > 0) {
        $s -= floor($z / 2);
        $p += $z;
        $s += floor($p / 2);
    }
    
    echo "$s\n";
}
?>