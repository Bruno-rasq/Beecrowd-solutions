<?php

$t = (int) readline();
while($t != 0){
    for($i = 0; $i < $t; $i++){
        $n = (int) readline();
        if(($n - 1) % 2 == 0) { echo 2 * $n - 1 . "\n"; } else { echo 2 * $n - 2 . "\n";}
    }
    $t = (int) readline();
}