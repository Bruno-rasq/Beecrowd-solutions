<?php
while ($line = fgets(STDIN)) {
    list($a, $b) = explode(' ', trim($line));
    $a = (int)$a;
    $b = (int)$b;
    $c = $a ^ $b;
    
    echo $c . "\n";
}